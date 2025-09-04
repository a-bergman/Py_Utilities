# Py_Utilities - Python Functions For Personal/Work Help

Python modules and scripts containing functions to help deal with tedious manual tasks.

-----

## Motivation

At work I often had to perform tasks such as moving files to a SFTP location, renaming batches of files, and comparing files. Performing those tasks by hand was error-prone, slow, and tedious so I began to develop functions to perform those tasks for me.

-----

## Dependencies

For these functions to run properly you should have the following installed:

- os
- shutil
- pandas
- filecmp
- hashlib
- collections

-----

## Contents

### Module -  `py_workspace_utils.py` Contents

| Function               | Description                                                          | Log? |
|:-----------------------|:---------------------------------------------------------------------|:----:|
| `move_file`            | Moves a file specified by name                                       | Yes  |
| `move_files`           | Loops through a directory and moves all files of the specified type  | Yes  |
| `rename_file`          | Renames a file specified by name                                     | Yes  |
| `rename_files`         | Renames files using names provided in a .csv file                    | Yes  |
| `compare_files_simple` | Compares two files to see if they are identical or not               | No   |
| `dir_duplicate_check`  | Loops through a directory and checks for any duplicates              | Yes  |

## Script(s)

### Script -  `py_file_organizer.py`

| Function                   | Description                                                          | Log? |
|:---------------------------|:---------------------------------------------------------------------|:----:|
| `create_new_directories()` | Moves a file specified by name                                       | TBA  |
| `py_file_organizer()`      | Loops through a directory and moves all files of the specified type  | TBA  |

-----

## How To Use

### Script(s)

- Copy `py_file_organizer.py` to the folder you will be organizing
- Update: file extensions, directories, and the `py_file_organizer()` function itself
- Open your command line and navigate to your directory `cd Desktop\Data\Messy_Folder`
- Run `python py_file_organizer.py`
- Visually validate the results

### Module(s)

- Create a local branch or clone and modify as desired. Additionally, I *strongly* recommend creating a local copy outside of your version  controlled location for regular use: modifications to an .ipynb file or the log folder probably shouldn't be tracked in Git.


-----

## Contributions

Pull requests are welcome, but for any major issues please open an issue first to discuss what needs to be changed.

-----

## Road Map

- [ ] Create versions of `py_workspace_utils.py` for cmd use.
- [ ] Improved error checking across all functions.
- [X] Adding logging for each function for tracking purposes.
- [X] Create script to organize directories.

-----

## Project Status

This repo is still a work in progress: code and/or formatting is added on a day-to-day basis.

-----

## Latest Updates

* `py_file_organizer.py`
    - 2025-09-04 - Added `py_file_organizer.py`; updated README.md

* `py_workspace_utils.py`

    - 2025-09-93 - Added `dir_duplicate_check()`; updated log file code for each; updated formatting in `py_workspace_utils.py`; updated `README.md`
    - 2025-09-02 - Added code that creates a `log.txt` for every function that modifies a file; updated docstrings/comments in `py_workspace_utils.py`; updated `README.md`
    - 2025-08-29 - Added `rename_files()` & `compare_files_simple()`; updated docstrings/comments in `py_workspace_utils.py`; updated `README.md`
    - 2025-08-28 - Added `rename_file()`; updated Road Map section in `README.md`
    - 2025-08-27 - Added `move_files()`; updated comments in the module; updated and added content to `README.md`
    - 2025-08-26 - Project initiation, initial commit of work; added `move_file()`
