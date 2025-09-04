import os
import shutil

## Last Updated    : 2025-09-25
## Last Updated By : a-bergman

# analyst = "a-bergman"

"""
This script is currently (as of 9/25/2025) configured to handle files I happened to have on hand. The overall
idea is that this will need to be modified depending on the file is pasted in to. I.e. the analyst will need
to update/add/remove the file extensions, directory names, and the list of directories in lines 13 to 26 as
well as in `py_file_organizer()` itself.
"""

## TO DO
# Test to see what happens if the directories already exist
## TO DO
# Add logging for this script

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
    for directory in directories:
        folder=os.path.join(path,directory)
        if not os.path.exists(folder):
            os.mkdir(folder)

# Creating the folders
create_new_directories()

# Function to organize files into the directories made with `create_new_directories()`
def py_file_organizer():
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
    # Looping through the files in the cwd
    for file in files:
        # Using a series of if statements on purpose
        # `elif` would cause the code to stop, which is not desired
        # `.endswith()` can take multiple inputs if they're passed as a tuple
        # Each `if` essentially just adds the directory to the cwd
        if file.endswith(tuple(data_ext)):
            source=os.path.join(path,file)
            destination=os.path.join(path,data_dir,file)
            shutil.move(source,destination)
        if file.endswith(tuple(code_ext)):
            source=os.path.join(path,file)
            destination=os.path.join(path,code_dir,file)
            shutil.move(source,destination)
        if file.endswith(tuple(txt_ext)):
            source=os.path.join(path,file)
            destination=os.path.join(path,txt_dir,file)
            shutil.move(source,destination)
        if file.endswith(tuple(msft_ext)):
            source=os.path.join(path,file)
            destination=os.path.join(path,msft_dir,file)
            shutil.move(source,destination)

py_file_organizer()