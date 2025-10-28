# Python CLITimer

**Python CLITimer** is a lightweight command-line tool for tracking time spent on different tasks or subjects.  
It allows users to start and stop sessions directly in the terminal and automatically logs all entries to a daily text file.

## 🕒 Description
The program is designed to help you measure how long you spend on specific activities.  
Each session starts when you enter a task name and ends when you stop it with **Ctrl+C**.  
The tool then records the duration and saves it to a text file, grouped by date.

## ⚙️ Features
- Start and stop time tracking sessions easily via the command line  
- Automatically logs session details (name, start, end, total time)  
- Supports manual time adjustments after session end  
- Calculates total time spent per day  
- Works on Windows and Linux
- No external dependencies

## 🧩 Technologies Used
- **Python 3.x**  
- Modules: `datetime`, `time`, `signal`, `os`, `threading`

## 🚀 How to Run
1. Clone or download the repository.  
2. Run the script from the terminal:
   ```bash
   python tracker.py
   ```
3. Enter the name of the task you’re working on.
   - Press Ctrl+C to end a session.
   - Enter (q) to quit the program.
   - Enter (p) to print all times recorded today.

## 🔍 Example
```bash
Please enter the subject you're working on: Study Python
Working on: Study Python
Started at: 15:42:01
Press STRG+C to end session
^C
Ended Session
Time tracked: 37.25 Minutes
Total Time (until now): 102.50
```

## 🧾 Output
```bash
Name: Study Python | Start Time: 15:42:01 | End Time: 16:19:16 | Total Time: 37.25
Name: Write Report | Start Time: 17:02:12 | End Time: 17:47:22 | Total Time: 45.17
Total Time: 82.42
```

## 🏫 Project Background
This tool was created as a personal utility to track daily focus and productivity time in a simple, distraction-free way.
