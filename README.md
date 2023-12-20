# **Zoom Meeting Scheduler**

This Python script facilitates scheduling and automatic joining of Zoom meetings based on data from an Excel file.

## Running & Using the Script
🐍 **Python 3.11** is recommended.

1. Install required packages using:
   ```
   pip install openpyxl webbrowser schedule
   ```
   
2. Prepare the Zoom meeting schedule in an Excel file named `zoom_meets.xlsx`.
   
   Structure the Excel file as follows:
   - Column 1: Zoom meeting name
   - Column 2: Zoom meeting link
   - Column 3: Meeting Time
   - Column 4: Day of the week
     - Use `M` for Monday, `T` for Tuesday, `Th` for Thursday, `F` for Friday.
     - If a meeting spans multiple days, separate the days by spaces. For example:
       - `M T` for meetings on Monday and Tuesday
       - `Th F` for meetings on Thursday and Friday

3. Run the script using:
   ```
   python main.py
   ```

At the scheduled times, the script will automatically open the Zoom meetings using the default web browser. 
If you want to automatically run the script at system startup, read the next sections.

## Creating Executable (Windows)

To convert `main.py` into a standalone executable file on Windows:

1. **Install PyInstaller:**

   If you haven't installed PyInstaller yet, you can do so via pip:
   ```bash
   pip install pyinstaller
   ```

2. **Create the Executable:**

   Open Command Prompt and navigate to the directory containing `main.py`. Then, use PyInstaller to create the executable:
   ```bash
   pyinstaller --onefile main.py
   ```

   This generates a standalone `main.exe` file in the `dist` directory within your project folder.

3. **Run the Executable:**

   Double-click `main.exe` to run the script as an executable.

## Running at System Startup (Windows)
To run the script at system startup:

1. Create a shortcut for `main.exe`.
2. Press `Win + R`, type `shell:startup`, and press `Enter`. This opens the Startup folder.
3. Move or copy the created shortcut to this Startup folder.
