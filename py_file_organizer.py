import os
import shutil
import datetime

## Last Updated    : 2025-09-08
## Last Updated By : a-bergman

## TO DO
# Figure out a system to deal with duplicate files

# Logs stored in: `C:/Users/andre/Documents/Logs/`

# Analyst should add their name in a similar format
analyst = "andrew.bergman"

"""
This script is currently (as of 9/05/2025) configured to handle files I happened to have on hand. The overall
idea is that this will need to be modified depending on the file is pasted in to. I.e. the analyst will need
to update/add/remove the file extensions, directory names, and the list of directories in lines 13 to 26 as
well as in `py_file_organizer()` itself.
"""
# File extensions w/ `.` - updated as needed for each directory
data_ext=[".csv",".json"]
code_ext=[".sql",".ipynb"]
txt_ext=[".txt"]
msft_ext=[".doc",".docx",".ppt",".pptx",".xls",".xlsx",".xlsb",".pdf"]

# Directory names - updated as needed for each directory
# DO NOT INCLUDE A SLASH OF ANY KIND
data_dir="data"
code_dir="code"
txt_dir="txt"
msft_dir="msft"

# List of directories - updated as needed for each directory
directories=[data_dir,code_dir,txt_dir,msft_dir]

# Getting the cwd
path=os.path.dirname(__file__)

# Getting all files in the cwd
files=os.listdir(path)

# Function to create the directories listed above
def create_new_directories():
    """
    Parameters:
    -----------
    None

    Description:
    ------------
    Creates the directories that files will be sorted into.

    Returns:
    --------
    N number of directories in `path` into which files will be sorted.
    """
    # Loops through the list of directories
    # Creates a new directory if it doesn't already exist
    for directory in directories:
        folder=os.path.join(path,directory)
        if not os.path.exists(folder):
            os.mkdir(folder)

# Creating the folders
create_new_directories()

# Function to organize files into the directories made with `create_new_directories()`
def file_organizer():
    """
    Parameters:
    -----------
    None

    Description:
    ------------
    Loops through the cwd and sorts files into the directories created in `create_new_directories()` based on their extensions

    Returns:
    --------
    None; files sorted into folders
    """
    # Getting the date in YYYY-MM-DD format &
    # the time in HH:MM format. Both are used for
    # naming the log file. The HH:MM is used to
    # prevent files being overridden
    today=datetime.datetime.today().strftime('%Y-%m-%d')
    run_time=str(datetime.datetime.now())[11:16].replace(":","꞉")
    # Creating a .txt file to act as our log file
    # Analyst needs to change the filepath locally
    with open(f"C:/Users/andre/Documents/Logs/{today}-{run_time}-py_file_organizer-log.txt","w") as py_logger:
        py_logger.write(f"Day              : {today} @ {str(datetime.datetime.now())[11:16]} \n")
        py_logger.write(f"Analyst          : {analyst} \n")
        py_logger.write(f"Script Run       : py_file_organizer.py: create_new_directories(); file_organizer() \n\n")
        py_logger.write(f"Directory        : {path} \n")
        py_logger.write(f"New Directories  : {directories} \n\n")
        # Looping through the files in the cwd
        for file in files:
            # Getting the exact time that each loop runs at
            dt_now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Using a series of if statements on purpose
            # `elif` would cause the code to stop, which is not desired
            # `.endswith()` can take multiple inputs if they're passed as a tuple
            # Each `if` essentially just adds the directory to the cwd
            # The a confirmation is printed to the cmd line and then to the log file
            if file.endswith(tuple(data_ext)):
                source=os.path.join(path,file)
                destination=os.path.join(path,data_dir,file)
                shutil.move(source,destination)
                print(f"{file} has been moved to {os.path.join(path,data_dir)}")
                py_logger.write(f">> {dt_now} - {file} moved to {os.path.join(path,data_dir)} \n")
            if file.endswith(tuple(code_ext)):
                source=os.path.join(path,file)
                destination=os.path.join(path,code_dir,file)
                shutil.move(source,destination)
                print(f"{file} has been moved to {os.path.join(path,code_dir)}")
                py_logger.write(f">> {dt_now} - {file} moved to {os.path.join(path,code_dir)} \n")
            if file.endswith(tuple(txt_ext)):
                source=os.path.join(path,file)
                destination=os.path.join(path,txt_dir,file)
                shutil.move(source,destination)
                print(f"{file} has been moved to {os.path.join(path,txt_dir)}")
                py_logger.write(f">> {dt_now} - {file} moved to {os.path.join(path,txt_dir)} \n")
            if file.endswith(tuple(msft_ext)):
                source=os.path.join(path,file)
                destination=os.path.join(path,msft_dir,file)
                shutil.move(source,destination)
                print(f"{file} has been moved to {os.path.join(path,msft_dir)}")
                py_logger.write(f">> {dt_now} - {file} moved to {os.path.join(path,msft_dir)} \n")

file_organizer()