import os
import shutil
import datetime

## Last Updated    : 2025-09-08
## Last Updated By : a-bergman

# Logs stored in: `C:/Users/andre/Documents/Logs/`

# Analyst should add their name in a similar format
analyst = "andrew.bergman"

"""
This script is currently (as of 9/08/2025) configured to handle files I happened to have on hand. The overall
idea is that this will need to be modified depending on the file is pasted in to. I.e. the analyst will need
to update/add/remove the directory names and the lists of directories in lines 24 to 25.
"""

# List of directories - updated as needed for each directory
mar2020_dir="2020-03"
aug2025_dir="2025-08"
sept2025_dir="2025-09"

# List of directories for logging & printing
directories = [mar2020_dir, aug2025_dir, sept2025_dir]
years=["2020","2025"]

# File types to ignore; always include `.py`
file_ignore=[".py",".ipynb"]
# Short name for files being ignored
file_ignore_type="Python"

# Getting the cwd
path=os.path.dirname(__file__)

# Getting all files in the cwd but ignoring existing subdirectories
files=[i for i in os.listdir(path) if os.path.isfile(i)]

# Function to organize files into the directories made with `create_new_directories()`
def date_organizer():
    # Getting the date in YYYY-MM-DD format &
    # the time in HH:MM format. Both are used for
    # naming the log file. The HH:MM is used to
    # prevent files being overridden
    today=datetime.datetime.today().strftime('%Y-%m-%d')
    run_time=str(datetime.datetime.now())[11:16].replace(":","꞉")
    # Creating a .txt file to act as our log file
    # Analyst needs to change the filepath locally
    with open(f"C:/Users/andre/Documents/Logs/{today}@{run_time}-py_date_organizer-log.txt","w") as py_logger:
        py_logger.write(f"Day              : {today} @ {str(datetime.datetime.now())[11:16]} \n")
        py_logger.write(f"Analyst          : {analyst} \n")
        py_logger.write(f"Script Run       : py_file_organizer.py: date_organizer() \n\n")
        py_logger.write(f"Directory        : {path} \n")
        py_logger.write(f"New Directories  : {directories} \n\n")
        # Looping through the files in the cwd
        for file in files:
            # We don't want to move the script file itself, so `.py` should always be in the `file_ignore` var
            if not file.endswith(tuple(file_ignore)):
                # Getting the exact time that each loop runs at
                dt_now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Getting the mdate for each for matching to folders
                created_date=str(datetime.datetime.fromtimestamp(os.path.getmtime(file)))[:7]
                # Using a series of if statements on purpose
                # `elif` would cause the code to stop, which is not desired
                # Then a confirmation is printed to the cmd line and then to the log file
                if created_date ="2020-03":
                    source=os.path.join(path,file)
                    destination=os.path.join(path,mar2020_dir,file)
                    shutil.move(source,destination)
                    print(f"{file} has been moved to {os.path.join(path,mar2020_dir)} \n")
                    py_logger.write(f"> {dt_now} - INFO: {file} moved to {os.path.join(path,mar2020_dir)} \n")
                if created_date=="2025-08":
                    source=os.path.join(path,file)
                    destination=os.path.join(path,aug2025_dir,file)
                    shutil.move(source,destination)
                    print(f"{file} has been moved to {os.path.join(path,aug2025_dir)} \n")
                    py_logger.write(f"> {dt_now} - INFO: {file} moved to {os.path.join(path,aug2025_dir)} \n")
                if created_date=="2025-09":
                    source=os.path.join(path,file)
                    destination=os.path.join(path,sept2025_dir,file)
                    shutil.move(source,destination)
                    print(f"{file} has been moved to {os.path.join(path,sept2025_dir)} \n")
                    py_logger.write(f"> {dt_now} - INFO: {file} moved to {os.path.join(path,sept2025_dir)} \n")
            else:
                # Printing a warning for the files we ignore
                print(f"WARN: ignoring {file_ignore_type} file {file} \n")
                py_logger.write(f"> {dt_now} - WARN : Ignoring {file_ignore_type} file: {file} \n")

# Executing the function
date_organizer()