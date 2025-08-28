# Py_Utilities - Python Functions For Personal/Work Help

Multiple Python modules containing functions to help deal with tedious manual tasks.

-----

## Motivation

At work I often had to perform tasks such as moving files to a SFTP location, renaming batches of files, and comparing files. Performing those tasks by hand was error-prone, slow, and tedious so I began to develop functions to perform those tasks for me.

-----

## Dependencies

For these functions to run properly you should have the following installed:

- os
- shutil

-----

## `py_workspace_utils.py` Contents

| Function      | Description                                                          |
|:--------------|:---------------------------------------------------------------------|
| `move_file`   | Moves a file specified by name                                       |
| `move_files`  | Loops through a directory and moves all files of the specified type  |
| `rename_file` | Renames a file specified by name


-----

## Contributions

Pull requests are welcome, but for any major issues please open an issue first to discuss what needs to be changed.

-----

## Road Map

- Adding logging for each function for tracking purposes
- Improved error checking across all functions

-----

## Project Status

This repo is still a work in progress: code and/or formatting is added on a day-to-day basis.

-----

## Latest Updates

* `py_workspace_utils.py`

    - 2025-08-28 - Added `rename_file()`; updated Road Map section in `README.md`
    - 2025-08-27 - Added `move_files()`; updated comments in the module; updated and added content to `README.md`
    - 2025-08-26 - Project initiation, initial commit of work; added `move_file()`
