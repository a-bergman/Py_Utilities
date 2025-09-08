import os
import datetime

## Last Updated    : 2025-09-08
## Last Updated By : andrew bergman-bergman

"""
In this script, I've chosen to use the os.path.getmtime() function. Please read this stackoverflow thread
that explains the difference between the two:

https://stackoverflow.com/questions/32010724/the-time-functions-time-getmtime-and-time-getctime-gives-the-same-result

To summarize:

os.path.getmtime() - Time when file *data* last modified.  Changed by the `mkdir`, `mkfifo`, `mknod`, `utimes`, `write` & system calls.

os.path.getctime() - Time when file *status* was last changed (inode data modification).  Changed by the `chflags`, `chmod`, `chown`,
                     `creat`, `link`, `mkdir`, `mkfifo`, `mknod`, `rename`, `rmdir`, `symlink`, `truncate`, `unlink`, `utimes`, 
                     `write` & `writev` system calls.
"""

# Logs stored in: `C:/Users/andre/Documents/Logs/`

# Analyst should add their name in a similar format
analyst = "andrew.bergman"

# Getting the cwd
path=os.path.dirname(__file__)

# Function to get the mdate for each file in `path`
def get_mdatetime(path):
    """
    Parameters:
    -----------
    path : path of the current working directory where work is being done : str : :

    Description:
    ------------
    Loops through the current working directory and extracts the mtime for each file and saves them to a list.

    Returns:
    --------
    A list containing the unique mtimes from the current working directory; prints a confirmation.
    """
    # Empty list to be filled with the mtime
    file_mdate = []
    # Looping through the current path to find mtimes
    for file in os.listdir(path):
        # Extracting the mtime & converting to a YYYY-MM format for the directory name
        created = os.path.getmtime(file)
        file_created = str(datetime.datetime.fromtimestamp(created))[:7]
        # Appending to the mdate list
        file_mdate.append(file_created)
    # This is hacky and produces an unordered list, but that's not
    # important as the file explorer will display them in alphabetically
    new_directories = list(set(file_mdate))
    return new_directories

# Reusing this from `py_file_organizer.py`
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
    # Getting the date in YYYY-MM-DD format &
    # the time in HH:MM format. Both are used for
    # naming the log file. The HH:MM is used to
    # prevent files being overridden
    today=datetime.datetime.today().strftime('%Y-%m-%d')
    run_time=str(datetime.datetime.now())[11:16].replace(":","꞉")
    # Executing the get_mdatetime() within this function to directly get the new directories and saving
    # them to a var so they can be printed as well
    mdate_directories = get_mdatetime(path=path)
    # Looping through the directory name results
    for directory in mdate_directories:
        # Defining a new directory for each and
        # creates a new directory if one doesn't
        # already exist
        dt_now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        folder=os.path.join(path,directory)
        if not os.path.exists(folder):
            os.mkdir(folder)
    # Creating a .txt file to act as our log file
    # Analyst needs to change the filepath locally
    with open(f"C:/Users/andre/Documents/Logs/{today}-{run_time}-py_mdate_folder-log.txt","w") as py_logger:
        py_logger.write(f"Day              : {today} @ {str(datetime.datetime.now())[11:16]} \n")
        py_logger.write(f"Analyst          : {analyst} \n")
        py_logger.write(f"Script Run       : py_file_organizer.py: get_mdatetime(); create_new_directories() \n\n")
        py_logger.write(f"Directory        : {path} \n\n")
        py_logger.write(f">> {dt_now} - New Folders Created: {mdate_directories} \n\n")
        # Looping through the files in the cwd
    # Printing a confirmation message with the names of the new directories
    print("Created New Directories:")
    print("------------------------")
    print(*mdate_directories, sep="\n")

create_new_directories()