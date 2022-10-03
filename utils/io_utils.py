"""
io_utils.py - Helper functions for reading and writing to cohort files
"""

import json
from pathlib import Path


def create_new_json_file(data: dict, filename: str) -> bool:
    """ Creates a new JSON file and writes data to it

    Args:
        data (dict):
        filename (str):

    Returns:
        bool: True if the file was successfully created
              False otherwise

    Todo:
        - deal with False return conditions
    """
    with open(filename, "w") as openfile:
        json.dump(obj=data, fp=openfile, indent="")

    return True


def update_json_file(data: dict, filename: str) -> bool:
    """ """
    pass


def read_from_json_file(filepath: Path) -> dict:
    """ Read the content of a .json file

    Args:
        filepath (Path):

    Returns:
        dict:

    Todo:
        - check if the file exists first
    """
    with open(file=filepath, mode='r') as openfile:
        return json.load(openfile)
