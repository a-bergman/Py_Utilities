import os
import sys
import argparse
import datetime
import hashlib
from collections import Counter

## Last Updated    : 2025-11-18
## Last Updated By : andrew-bergman

# Analyst will need to update their paths
# Logs stored in: `C:/Users/andre/Documents/Logs/` (Windows)
# Logs stored in: `/home/abergman/Documents/Python Vault/Logs/` (Ubuntu)

## TO DO
# Figure out a system to deal with duplicate files

# Analyst should add their name in a similar format
analyst = "andrew.bergman"

def dir_duplicate_check(path):
    """
    Parameters:
    -----------
    path : path to destination directory   : str : :

    Description:
    ------------
    Loops through all files in the `path` directory and uses a md5 has to check for duplicates.

    Returns:
    --------
    A record file in `/logs` with the date, time, and function name in the title of the file; prints results if duplicates are found.
    
    The record file and print statement will be empty if no duplicates are found.

    """
    # Getting the date in YYYY-MM-DD format &
    # the time in HH:MM format. Both are used for
    # naming the log file. The HH:MM is used to
    # prevent files being overridden
    today=datetime.datetime.today().strftime('%Y-%m-%d')
    run_time=str(datetime.datetime.now())[11:16].replace(":","꞉")
    # Defining the full path to the file being moved
    # Create an empty dictionary
    file_dict=dict()
    # Validating the path of files to be checked
    if os.path.isdir(path):
        # Looping through the directory
        for file in os.listdir(path):
            # Creating a full filepath for each file
            full_path=os.path.join(path,file)
            # Reading each file and creating a md5 has for each
            # and then adding each file name and md5 as key:value
            # pairs to the dictionary
            file_hash=hashlib.md5(open(full_path,"rb").read()).hexdigest()
            file_dict[file]=file_hash
    else:
        sys.exit(f"ERROR: {path} is not a valid directory.")
    # Creating a Counter
    count_dict=Counter(file_dict.values())
    # Extracting the dict values and counting
    # If the hash value is duplicated there are duplicate files then saving duplicates to a new variable
    results=[key for key,value in file_dict.items() if count_dict[value]>1]
    # Writing a confirmation to the log file for the renamed file
    # No files are being modified, but it is good to have a record for posterity
    # Analyst should update the file path
    with open(f"/home/abergman/Documents/Python Vault/Logs/{today}@{run_time}-dir_duplicate_check-record.txt","w") as py_logger:
        dt_now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        py_logger.write(f"Day..........: {today} @ {str(datetime.datetime.now())[11:16]} \n")
        py_logger.write(f"Analyst......: {analyst} \n")
        py_logger.write(f"Script Run...: py_dir_dup_check.py: dir_duplicate_check() \n\n")
        py_logger.write(f"Directory....: {path} \n\n")
        # {results} will be an empty list in the file if there aren't duplicates
        py_logger.write(f"> {dt_now} - INFO: Duplicates = {results} \n\n")
    # Print message for the user
    print(f">> Checking {path} For Duplicates",sep="\n")
    print(f">> No File Names Will Be Printed If There Are None",sep="\n")
    print(f">> -----------------------------------------------",sep="\n")
    print(*results,sep="\n")

# When we execute this, we want to make sure all args are present
# The TRY/EXCEPT will raise an error with a missing argument
# https://medium.com/@evaGachirwa/running-python-script-with-arguments-in-the-command-line-93dfa5f10eff
if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Loops through all files in `path` directory and uses a md5 hash to check for duplicates")
    try:
        # Making entry in the command line easier
        parser.add_argument("--path",required=True,type=str,help="enter a path to the dir to be checked")
        args=parser.parse_args()
        # Defining the args for the function
        path=args.path
        print(dir_duplicate_check(path))
    except TypeError:
        print("Please make sure your arguments are correct")
