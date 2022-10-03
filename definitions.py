"""
definitions.py
"""

import os
from pathlib import Path

# ---------------------------------------------------------------------------------------#
# Paths
# ---------------------------------------------------------------------------------------#

PATH_ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))

COHORT_DIRECTORY_PATH = Path.joinpath(PATH_ROOT_DIR, "json/cohorts.json")


# ---------------------------------------------------------------------------------------#
# Constants
# ---------------------------------------------------------------------------------------#

CURRENT_VERSION = "alpha"

