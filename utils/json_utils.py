""" json_utils.py - Helper functions for reading and writing to cohort files """

import json
import os
from pathlib import Path

from definitions import COHORT_DIR, COHORT_REGISTER_PATH


def update_cohort_register(new_cohort_name: str):
    """ """
    cohort_register = read_from_json_file(COHORT_REGISTER_PATH)
    if 'cohorts' in cohort_register:
        cohorts = list(cohort_register['cohorts'])
        cohorts.append(new_cohort_name)
        cohort_register['cohorts'].append(new_cohort_name)
    else:
        cohorts = [new_cohort_name]


def write_to_json_file(data: dict, filepath: Path) -> bool:
    """ Writes data to a JSON file.

    If the file already exists, the data will be appended to the end.

    Args:
        data (dict):
        filepath (Path):

    Returns:
        bool: True if the file was successfully created
              False otherwise

    Todo:
        - deal with False return conditions
    """
    with open(filepath, "a") as openfile:
        json.dump(obj=data, fp=openfile, indent="")

    return True


def read_from_json_file(filepath: Path) -> dict:
    """ Read the content of a .json file.

    Args:
        filepath (Path):

    Returns:
        dict:

    Todo:
        - check if the directory exists first
        - do I need to check if the file exists first, or does it get made when I first write to it?
    """
    with open(file=filepath, mode='r') as openfile:
        return json.load(openfile)


def get_path_to_cohort_json_file(cohort: str) -> Path:
    """ Returns a filepath to a .json file describing a cohort of students.

    If the file does not exist when this method is called, it will create it.

    Args:
        cohort (str): The name of the cohort.

    Returns:
        Path: A Path object that points to the file "filename.json".
    """
    cohort = cohort.lower().replace(" ", "_")
    cohort += ".json"

    if not os.path.exists(COHORT_DIR):
        os.makedirs(COHORT_DIR)

    filepath = Path.joinpath(COHORT_DIR, cohort)

    return filepath
