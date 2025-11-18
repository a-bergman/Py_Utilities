import os
import sys
import argparse
import datetime
import pandas as pd

## Last Updated    : 2025-11-18
## Last Updated By : a-bergman

# Analyst will need to update their paths
# Logs stored in: `C:/Users/andre/Documents/Logs/` (Windows)
# Logs stored in: `/home/abergman/Documents/Python Vault/Logs/` (Ubuntu)

## TO DO
# Figure out a system to deal with duplicate files

# Analyst should add their name in a similar format
analyst = "andrew.bergman"

def rename_files(file_path,name_path,name_csv):
    """
    Parameters:
    ----------
    file_path : path to directory where files to be renamed are stored              : str : :
    name_path : path to directory where .csv file containing name mapping is stored : str : :
    name_csv  : name of the .csv file that contains the old-new name mapping        : str : :

    Description:
    ------------
    Reads the specified .csv file and renames files in the file_path based on the values in the .csv.

    The name of the .csv file does not matter, but it must have two columns called `old_name` and `new_name`.

    Returns:
    --------
    A log file in `/logs` with the date, time, and function name in the title of the file; prints confirmation.
    """
    # TO DO
    # Add a check to make sure that
    # files with the new names do
    # not already exist in the
    # `file_path` location.

    # Getting the date in YYYY-MM-DD format &
    # the time in HH:MM format. Both are used for
    # naming the log file. The HH:MM is used to
    # prevent files being overridden
    today=datetime.datetime.today().strftime('%Y-%m-%d')
    run_time=str(datetime.datetime.now())[11:16].replace(":","꞉")
    # Creating file path to name_csv
    names=os.path.join(name_path, name_csv)
    # Making sure it exists
    if os.path.isfile(names):
        # Reading the .csv in
        # Converting to dictionary
        name_df=pd.read_csv(names)
        # .csv must have those two column headers
        name_dict=dict(zip(name_df["old_name"],name_df["new_name"]))
        # Creating a .txt file to act as our log file
        # The analyst should update this path
        with open(f"/home/abergman/Documents/Python Vault/Logs/{today}@{run_time}-rename_files-log.txt","w") as py_logger:
            # Adding the location of the name dictionary & files to be renamed
            py_logger.write(f"Day...................: {today} @ {str(datetime.datetime.now())[11:16]} \n")
            py_logger.write(f"Analyst...............: {analyst} \n")
            py_logger.write(f"Script Run............: py_rename_files.py: rename_files() \n\n")
            py_logger.write(f"File Location ........: {file_path} \n")
            py_logger.write(f"File Mapping Location.: {name_path} \n")
            py_logger.write(f"File Mapping .csv.....: {name_csv} \n\n")
            # Looping through the directory where the files to be renamed are
            for file in os.listdir(file_path):
                # Getting the exact time that each loop runs at
                dt_now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Finding the ones that are also key values
                # Ignores files that aren't specified to be renamed
                if file in name_dict.keys():
                    # Extracting the value from the key:value pair
                    # Renaming the file(s)
                    value=name_dict.get(file)
                    old_name=os.path.join(file_path,file)
                    new_name=os.path.join(file_path,value)
                     # `os.replace` is preferred to `os.rename` in Python versions >3.3
                    os.replace(old_name, new_name)
                    # Printing confirmation
                    print(f"{file} has been renamed {value}")
                    # Writing a confirmation to the log file for each renamed file
                    py_logger.write(f"> {dt_now} - INFO: {file} has been renamed to: {value} \n")
    else:
        sys.exit(f"ERROR: {names} is not a valid file path")

# When we execute this, we want to make sure all args are present
# The TRY/EXCEPT will raise an error with a missing argument
# https://medium.com/@evaGachirwa/running-python-script-with-arguments-in-the-command-line-93dfa5f10eff
if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Renames files in `fpath` based on `ncsv` in `npath`")
    try:
        # Making entry in the command line easier
        parser.add_argument("--fpath",required=True,type=str,help="enter a path to the destination dir")
        parser.add_argument("--npath",required=True,type=str,help="enter a path to the source dir")
        parser.add_argument("--ncsv",required=True,type=str,help="enter type of file to be moved")
        args=parser.parse_args()
        # Defining the args for the function
        fpath=args.fpath
        npath=args.npath
        ncsv=args.ncsv
        print(rename_files(fpath,npath,ncsv))
    except TypeError:
        print("Please make sure your arguments are correct")