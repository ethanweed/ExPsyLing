"""
data_wrangling.py

This module contains functions to assist in cleaning and organizing data exported from 
a JATOS server.

Functions:

collect_data_files
    this organizes data from a multi-component JATOS study that has been exported as a 
    JATOS Results Archive. The function walks the folder structure of the archive, renames
    files with participant ID and component ID numbers. NOTE: collect_data_files currently
    assumes that all participants complete components in the same order. Modifications will
    be needed for studies that randomize or alternate component order across participants.

parse_labjs_data
    Take the data from a lab.js experiment run on JATOS, which is exported in a weird,
    pseudo-JSON format, and put it in a pandas dataframe.

"""

# import dependencies
import os
import shutil
import jsonlines
import pandas as pd
from pathlib import Path



def collect_data_files(data_dir):
    """
    Rename data.txt files in study_result folders using participant ID and component number.

    Args:
        data_dir: (string) Root directory containing study_result folders

    Usage:
        data_wrangling.collect_data_files(data_dir)
    """
    root_path = Path(data_dir)

    # Find all study_result folders
    study_folders = sorted([d for d in root_path.iterdir() 
                           if d.is_dir() and d.name.startswith('study_result_')])

    for study_folder in study_folders:
        # Extract participant ID from folder name
        participant_id = study_folder.name.split('_')[2]

        # Find all comp-result folders and sort them
        comp_folders = sorted([d for d in study_folder.iterdir() 
                              if d.is_dir() and d.name.startswith('comp-result_')])

        # Rename data.txt files with component number (1-indexed)
        for component_num, comp_folder in enumerate(comp_folders, start=1):
            data_file = comp_folder / 'data.txt'

            if data_file.exists():
                new_filename = f"{participant_id}_{component_num}.txt"
                new_filepath = comp_folder / new_filename

                # Rename the file
                data_file.rename(new_filepath)
                print(f"Renamed: {data_file} -> {new_filepath}")
            else:
                print(f"Warning: {data_file} not found")
                
                

    # Create raw_data folder if it doesn't exist
    raw_data_folder = root_path / 'raw_data'
    raw_data_folder.mkdir(exist_ok=True)
    print(f"Created/verified folder: {raw_data_folder}\n")

    # Find all study_result folders
    study_folders = sorted([d for d in root_path.iterdir() 
                           if d.is_dir() and d.name.startswith('study_result_')])

    files_moved = 0

    for study_folder in study_folders:
        # Find all comp-result folders
        comp_folders = sorted([d for d in study_folder.iterdir() 
                              if d.is_dir() and d.name.startswith('comp-result_')])

        for comp_folder in comp_folders:
            # Look for renamed files (format: XXXX_Y.txt)
            for file in comp_folder.iterdir():
                if file.is_file() and file.suffix == '.txt':
                    # Move file to raw_data folder
                    destination = raw_data_folder / file.name
                    shutil.move(str(file), str(destination))
                    print(f"Moved: {file} -> {destination}")
                    files_moved += 1

    print(f"\nTotal files moved: {files_moved}\n")

    # Remove empty folders
    print("Removing empty folders...")
    folders_removed = 0

    for study_folder in study_folders:
        # Find all comp-result folders
        comp_folders = sorted([d for d in study_folder.iterdir() 
                              if d.is_dir() and d.name.startswith('comp-result_')])

        # Remove empty comp-result folders
        for comp_folder in comp_folders:
            if comp_folder.exists() and not any(comp_folder.iterdir()):
                comp_folder.rmdir()
                print(f"Removed: {comp_folder}")
                folders_removed += 1

        # Remove empty study_result folder
        if study_folder.exists() and not any(study_folder.iterdir()):
            study_folder.rmdir()
            print(f"Removed: {study_folder}")
            folders_removed += 1

    print(f"\nTotal folders removed: {folders_removed}")



def parse_labjs_data(raw, remove_meta_data = True):
    """
    Take the data from a lab.js experiment run on JATOS, which is exported in a weird,
    pseudo-JSON format, and put it in a pandas dataframe.

    Args: 
        raw: (string) Path to text file with labjs data
        remove_meta_data: (logical) if True, remove the first line of the dataframe, which contains 
        meta-data such as labjs version number, participant's device operating system, etc.
        Default is True.
    
    Usage:
        df = data_wrangling.parse_labjs_data(raw, True)

    """



    with open(raw, 'r') as f:
        first_line = f.readline()
        if '"labjs_version"' not in first_line:
            print('This file does not appear to be in lab.js format')
            return None

    i = 0                                                          # set counter variable "i" to zero

    with jsonlines.open(raw) as reader:                            # make a "reader" variable with the lab.js data (which is stored in "JSON" format)
        for line in reader:                                        # loop through every line in the lab.js JSON data
            if i == 0:                                             # check if i equals zero. If it does, then
                df = pd.DataFrame(line)                            # make a new pandas dataframe called "df" 
                i += 1                                             # add 1 to i
            else:                                                  # if i does not equal zero 
                df = pd.concat([df, pd.DataFrame(line)], ignore_index=True)           # get the next line of the json file, convert it to a dataframe, and stick it on the bottom of "df"                                           # add 1 to i
        print('labjs data found and imported 👍')
        return(df.drop(index=0) if remove_meta_data else df)          # after looping through all lines, return the dataframe "df", but drop the first line (index 0) if remove_meta_data is True. Otherwise, return the full dataframe with meta-data included.



def parse_jatos_data(raw):
    """
    Take the data from a non-lab.js experiment run on JATOS, which is exported in a weird,
    pseudo-JSON format, and put it in a pandas dataframe.

    Args: 
        raw: (string) Path to text file with data
        
    
    Usage:
        df = data_wrangling.parse_jatos_data(raw)
    """


    i = 0                                                          # set counter variable "i" to zero

    with jsonlines.open(raw) as reader:                            # make a "reader" variable with the lab.js data (which is stored in "JSON" format)
        for line in reader:                                        # loop through every line in the lab.js JSON data
            if i == 0:                                             # check if i equals zero. If it does, then
                df = pd.DataFrame([line])                            # make a new pandas dataframe called "df" 
                i += 1                                             # add 1 to i
            else:                                                  # if i does not equal zero 
                df = pd.concat([df, pd.DataFrame([line])], ignore_index=True)           # get the next line of the json file, convert it to a dataframe, and stick it on the bottom of "df" 
    return df

