"""
This module contains various functions designed to help with tedious manipulation of files.

Last Update   : 2025-08-29
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
import filecmp

import pandas as pd

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
    file_path=os.path.join(src_path, file_name)
    # Making sure the destination is valid
    if os.path.isdir(dst_path):
        # Making sure the source location is valid
        if os.path.isdir(src_path):
            # Making sure the file exists in the source
            if os.path.isfile(file_path):
                # Defining the destination location
                # Printing confirmation of success
                destination=os.path.join(dst_path,file_name)
                shutil.move(file_path, destination)
                print(f"{file_name} has been successfully moved: {destination}")
            else:
                print(f"The file {file_path} does not exist.")
        else:
            print(f"ERROR: Source {src_path} is an invalid directory.")
    else:
        print(f"ERROR: Destination {dst_path} is an invalid directory.")

def move_files(dst_path, src_path, file_type):
    """
    Parameters:
    -----------
    dst_path  : path to destination directory     : str :        :
    src_path  : path of the source directory      : str :        :
    file_type : file extension, including the `.` : str : ".csv" :

    Description:
    ------------
    Loops through the source directory looking for files that match `file_type` and moves them to the destination directory and prints a confirmation.

    Returns:
    --------
    N/A; confirmation that file was moved to the destination.
    """
    # TO DO:
    # Figure out a way to handle the
    # file type missing error messaging.
    # I would like it to print the error
    # message only if the file isn't found
    # at the beginning of the `for` loop.
    # TO DO:
    # Add support for multiple file types.
    
    # Validating the destination
    if os.path.isdir(dst_path):
        # Validating the source
        if os.path.isdir(src_path):
            # Looping through the source directory
            for file in os.listdir(src_path):
                # Getting the file name and type for each
                file_name=os.fsdecode(file)
                # Selecting the files that match input
                if file_name.endswith(file_type):
                    # Creating file paths and moving files
                    source=os.path.join(src_path,file_name)
                    destination=os.path.join(dst_path,file_name)
                    shutil.move(source,destination)
                    print(f"{file_name} successfully moved to {dst_path}")
                else:
                    print(f"ERROR: File type '{file_type}' not found in {src_path}.")
                    break
        else:
            print(f"ERROR: Source {src_path} is an invalid directory.")
    else:
         print(f"ERROR: Destination {dst_path} is an invalid directory.")

def rename_file(path, old_name, new_name):
    """
    Parameters:
    -----------
    path     : working directory where file is                       : str : :
    old_name : current name of file to be renamed with the extension : str : :
    new_name : new name of file to be renamed with the extension     : str : :

    Description:
    ------------
    Renames a file in the specified directory.

    Returns:
    --------
    N/A; a confirmation that the rename was successful
    """
    # TO DO
    # Add support to validate file extensions are equal
    # Add support to validate file path exists
    
    # Creating file paths
    old_file = os.path.join(path, old_name)
    new_file = os.path.join(path, new_name)
    # Validating the a file with the new name doesn't already exist
    if not os.path.isfile(new_file):
        # Validating the existing file exists
        if os.path.isfile(old_file):
            # os.replace is preferred to `os.rename` in Python versions >3.3
            os.replace(old_file, new_file)
            print(f"{old_name} has been renamed {new_name}")
        else:
            print(f"ERROR: {old_name} does not exist in {path}")
    else:
        print(f"ERROR: {new_name} already exists in {path}")

def rename_files(file_path, name_path, name_csv):
    """
    Parameters:
    ----------
    file_path : path to directory where files to be renamed are stored              : str : :
    name_path : path to directory where .csv file containing name mapping is stored : str : :
    name_csv  : name of the .csv file that contains the old-new name mapping        : str : :

    Description:
    ------------
    Reads the specified .csv file and renames files in the file_path based on the values in the .csv.

    Returns:
    --------
    N/A; prints a confirmation for each file renamed successfully
    """
    # TO DO
    # Add a check to make sure that
    # files with the new names do
    # not already exist in the
    # `file_path` location.

    # Creating file path to name_csv
    names = os.path.join(name_path, name_csv)
    # Making sure it exists
    if os.path.isfile(names):
        # Reading the .csv in
        # Converting to memory
        name_df=pd.read_csv(names)
        # .csv must have those two column headers
        name_dict=dict(zip(name_df["old_name"], name_df["new_name"]))
        # Looping through the directory where the files to be renamed are
        for file in os.listdir(file_path):
            # Finding the ones that are also key values
            # Ignores files that aren't specified to be renamed
            if file in name_dict.keys():
                # Extracting the value from the key:value pair
                # Renaming the file(s)
                value=name_dict.get(file)
                old_name=os.path.join(file_path, file)
                new_name=os.path.join(file_path, value)
                # `os.replace` is preferred to `os.rename` in Python versions >3.3
                os.replace(old_name, new_name)
                # Printing confirmation
                print(f"{file} has been renamed {value}")
    else:
        print(f"ERROR: {names} is not a valid file path")

def compare_files_simple(file_a, file_b):
    """
    Parameters:
    -----------
    file_a : full file path of the first of the two files being compared  : str : :
    file_b : full file path of the second of the two files being compared : str : :

    Descriptions:
    -------------
    Checks the sizes of the two files and if they are different it compares the two using file statistics.

    Returns:
    --------
    N/A; prints statement displaying if they are identical or not. 
    """
    # TO DO
    # Add a method arg to support
    # using a hash based comparison
    # method.
    if os.path.isfile(file_a) and os.path.isfile(file_b):
        if os.path.getsize(file_a) == os.path.getsize(file_b):
            if filecmp.cmp(file_a, file_b) == True:
                print(f"REPORT: {file_a.split("/")[-1]} and {file_b.split("/")[-1]} are are identical")
            elif filecmp.cmp(file_a, file_b) == False:
                print(f"REPORT: {file_a.split("/")[-1]} and {file_b.split("/")[-1]} are different")
            else:
                print("ERROR: Please Check Your Inputs")
        else:
            print(f"REPORT: {file_a.split("/")[-1]} and {file_b.split("/")[-1]} are different")
    else:
        print(f"ERROR: Please check your inputs")