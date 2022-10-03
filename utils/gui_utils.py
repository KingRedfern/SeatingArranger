""" gui_utils.py - Utility functions and classes for the GUI """

import enum


# ---------------------------------------------------------------------------------------#
# Class definition
# ---------------------------------------------------------------------------------------#

class GUIState(enum.Enum):
    NONE = 0
    START = 1
    SELECT_COHORT = 2
