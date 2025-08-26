"""
This module contains various functions designed to help with tedious manipulation of files.

Last Update   : 2025-08-26
Last Update By: a-bergman

"""

"""

The docstrings for each function contain the following:

- parameters  : values which must be entered
- description : what each function does
- returns     : the output of each function

The parameters section of each docstring is set up as:

parameter : definition : type : possible values (if applicable)

"""

 
#  Standard Imports
import os
import shutil

# Move Single File

def move_file(dst_path,src_path,file_name):
    """
    Parameters:
    -----------
    dst_path  : path to destination directory   : str : :
    src_path  : path of the source directory    : str : :
    file_name : name of the file with extension : str : :

    Description:
    ------------
    Moves the named file from the source directory to the destination directory and prints a confirmation.

    Returns:
    --------
    N/A; confirmation that file was moved to the destination.
    """
    # TO DO:
    # A better way to handle validating 
    # each argument separately to avoid
    # the nested if statements.

    # Defining the full path to the file being moved
    file_path = os.path.join(src_path, file_name)
    # Making sure the destination is valid
    if os.path.isdir(dst_path):
        # Making sure the source location is valid
        if os.path.isdir(src_path):
            # Making sure the file exists in the source
            if os.path.isfile(file_path):
                # Defining the destination location
                # Printing confirmation of success
                destination = os.path.join(dst_path,file_name)
                shutil.move(file_path, destination)
                print(f"{file_name} has been successfully moved: {destination}")
            else:
                print(f"The file {file_path} does not exist.")
        else:
            print(f"ERROR: Source {src_path} is an invalid directory.")
    else:
        print(f"ERROR: Destination {dst_path} is an invalid directory.")