import os
import sys
import argparse
import shutil
import datetime

## Last Updated    : 2025-11-18
## Last Updated By : a-bergman

# Analyst will need to update their paths
# Logs stored in: `C:/Users/andre/Documents/Logs/` (Windows)
# Logs stored in: `/home/abergman/Documents/Python Vault/Logs/` (Ubuntu)

## TO DO
# Figure out a system to deal with duplicate files

# Analyst should add their name in a similar format
analyst = "andrew.bergman"

def move_files(dst_path,src_path,file_type):
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
    A log file in `/logs` with the date, time, and function name in the title of the file; prints confirmation.
    """
    # TO DO:
    # Figure out a way to handle the
    # file type missing error messaging.
    # I would like it to print the error
    # message only if the file isn't found
    # at the beginning of the `for` loop.
    # TO DO:
    # Add support for multiple file types.
    
    # Getting the date in YYYY-MM-DD format &
    # the time in HH:MM format. Both are used for
    # naming the log file. The HH:MM is used to
    # prevent files being overridden
    today=datetime.datetime.today().strftime('%Y-%m-%d')
    run_time=str(datetime.datetime.now())[11:16].replace(":","꞉")
    # Validating the destination
    if os.path.isdir(dst_path):
        # Validating the source
        if os.path.isdir(src_path):
           # Creating a .txt file to act as our log file
           # Should be updated by the analyst
           with open(f"/home/abergman/Documents/Python Vault/Logs/{today}@{run_time}-move_files-log.txt","w") as py_logger:
            # Adding the location of the name dictionary & files to be renamed
            py_logger.write(f"Day..............: {today} @ {str(datetime.datetime.now())[11:16]} \n")
            py_logger.write(f"Analyst..........: {analyst} \n")
            py_logger.write(f"Script Run.......: py_move_files.py: move_files() \n\n")
            py_logger.write(f"Source Path......: {src_path} \n")
            py_logger.write(f"Destination Path.: {dst_path} \n")
            py_logger.write(f"File Type........: {file_type} \n\n")
            # Looping through the source directory
            for file in os.listdir(src_path):
                # Getting the exact time that each loop runs at
                dt_now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Getting the file name and type for each
                file_name=os.fsdecode(file)
                # Selecting the files that match input
                if file_name.endswith(file_type):
                    # Creating file paths and moving files
                    source=os.path.join(src_path,file_name)
                    destination=os.path.join(dst_path,file_name)
                    shutil.move(source,destination)
                    # Printing a confirmation
                    print(f"{file_name} successfully moved to {dst_path}")
                    # Writing a confirmation to the log file for each renamed file
                    py_logger.write(f"> {dt_now} - INFO: {file} moved from {src_path} to {dst_path} \n")
        else:
            sys.exit(f"ERROR: Source {src_path} is an invalid directory.")
    else:
         sys.exit(f"ERROR: Destination {dst_path} is an invalid source directory.")

# When we execute this, we want to make sure all args are present
# The TRY/EXCEPT will raise an error with a missing argument
# https://medium.com/@evaGachirwa/running-python-script-with-arguments-in-the-command-line-93dfa5f10eff
if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Loops through the source for files of `file_type` and moves them to the destination")
    try:
        # Making entry in the command line easier
        parser.add_argument("--dst",required=True,type=str,help="enter a path to the destination dir")
        parser.add_argument("--src",required=True,type=str,help="enter a path to the source dir")
        parser.add_argument("--ftype",required=True,type=str,help="enter type of file to be moved")
        args=parser.parse_args()
        # Defining the args for the function
        dst=args.dst
        src=args.src
        type=args.ftype
        print(move_files(dst,src,type))
    except TypeError:
        print("Please make sure your arguments are correct")
