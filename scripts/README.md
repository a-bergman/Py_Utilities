# Background

This folder contains two types of scripts:

- traditional ones that are run from the command line;
  - These are complete
- ones that launch a GUI and then run the script.
  - `gui_rename_files.py` is complete; others have not been started


## Goals

The goal of this is to provide a basic script to be run from the command line as well as a more user-friendly variant of each via a GUI.

## Script Status

| Script                   | Status   | Notes |
| ------------------------ | -------- | ----- |
| `py_date_organizer.py` | Complete | N/A   |
| `py_dir_dup_check.py`  | Complete | N/A   |
| `py_file_organizer.py` | Complete | N/A   |
| `py_mdate_folder.py`   | Complete | N/A   |
| `py_move_files.py`     | Complete | N/A   |
| `py_rename_files.py`   | Complete | N/A   |

## GUI Status

| Script                 | Status      | Notes                                                                                        |
| ---------------------- | ----------- | -------------------------------------------------------------------------------------------- |
| `py_rename_files.py` | In Progress | 2026-04-13 - GUI done; script implemented but import needs to be fixed; need to add comments |

## How To Run

- For the plain scripts:
  - Navigate to the `scripts` folder in the command line
  - type `python3 sample_script.py --arg1 "" --arg2 ""` depending on the individual script
  - The script will print out its results and create a `log.txt` file
- For the GUI scripts
  - Navigate to the `scripts` folder in the command line
  - Type in `python3 gui_rename_files.py`
  - The GUI will launch and prompt you to select what's needed
  - The GUI will print its results and create a `log.txt` file
