"""
definitions.py
"""

import os
from pathlib import Path

# ---------------------------------------------------------------------------------------- #
# Paths
# ---------------------------------------------------------------------------------------- #

PATH_ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))

JSON_DIR = Path.joinpath(PATH_ROOT_DIR, "json")
COHORT_REGISTER_PATH = Path.joinpath(JSON_DIR, "cohort-register.json")
COHORT_DIR = Path.joinpath(JSON_DIR, "cohorts")


# ---------------------------------------------------------------------------------------- #
# Constants
# ---------------------------------------------------------------------------------------- #

CURRENT_VERSION = "alpha"
NEXT_BUTTON_TEXT = "Next"

EMPTY_SEAT_HISTORY: dict = {"adjacent seats": [], "same table": []}

