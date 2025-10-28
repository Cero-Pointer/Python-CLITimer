from threading import Thread
from datetime import datetime
import signal
import time
import os

class s():
    def __init__(self, subject, start, end, time):
        self.subject = subject
        self.time = time
        self.start = start
        self.end = end

start = None
end = None
not_stop = True
stop_handler = True
subjectList = []
subjectName = ""

# Signal handler for STRG+C
def handler(signum, frame):
    global stop_handler
    if(stop_handler == True):
        return
    print("\r", end="")
    print("Ended Session\n-------------------------------")
    end = datetime.now()
    diff = round((end - start).total_seconds()/60.0,2)
    print("Time tracked: "+str(diff)+" Minutes")
    adjust_time = input("If you want to adjust the time enter it now\n" +
                        "e.g 5 for +5 Minutes, -5 for -5 Minutes\n" +
                        "press enter to skip: ")
    if(adjust_time != ""):
        if(adjust_time.isdigit()):
            diff += int(adjust_time)
        elif(adjust_time[0] == '-'):
            if(diff - int(float(adjust_time.lstrip('-'))) > 0):
                diff -= int(float(adjust_time.lstrip('-')))
            else:
                diff = 0
    subject = s(subjectName, start, end, diff)
    subjectList.append(subject)
    print_and_write_subject_list()
    global not_stop
    not_stop = False
    stop_handler = True

# Clear console function
def clear_console():
    if os.name == "nt":  
        os.system("cls")
    else:                
        os.system("clear")

# Print and write subject list to file
def print_and_write_subject_list():
    time = datetime.now()
    f = open("times_{}_{}_{}.txt".format(time.day, time.month, time.year), "a")
    for i in subjectList:
        print("Name: ",i.subject, "| Start Time:", i.start.strftime("%H:%M:%S"),
        "| End Time: ", i.end.strftime("%H:%M:%S"), "| Total Time:", i.time)
        
    f.write("Name: {} | Start Time: {} | End Time: {} | Total Time {}\n"
    .format(subjectList[-1].subject, subjectList[-1].start.strftime("%H:%M:%S"),
    subjectList[-1].end.strftime("%H:%M:%S"), subjectList[-1].time))
    
    print("Total Time (until now): {}".format(str(round(calculateTotalTime(),2))))
    print("-------------------------------")
    f.close()

# Calculate total time from all subjects      
def calculateTotalTime():
    totalTime = 0
    for i in subjectList:
        totalTime += i.time
    return totalTime

q = False
signal.signal(signal.SIGINT, handler)

while not q:
    print("Enter (q) to quit, (p) to print all times today")
    subjectName = input("Please enter the subject you're working on: ")
    not_stop = True
    start = datetime.now()
    if(subjectName == "q"):
        clear_console()
        f = open("times_{}_{}_{}.txt".format(start.day, start.month, start.year), "a")
        f.write("Total Time: {}\n".format(str(round(calculateTotalTime(),2))))
        f.write("-------------------------------\n")
        f.close()
        break;
    elif(subjectName == "p"):
        f = open("times_{}_{}_{}.txt".format(start.day, start.month, start.year), "r")
        print(f.read())
        f.close()
        continue
    clear_console()
    print("Working on: " + subjectName)
    print("Started at: ",start.strftime("%H:%M:%S"))
    print("Press STRG+C to end session")
    stop_handler = False

    while not_stop:
        time.sleep(0.1)
        
