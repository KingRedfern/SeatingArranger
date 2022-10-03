""" gui_utils.py - Utility functions and classes for the GUI """

import enum


# ---------------------------------------------------------------------------------------- #
# Class definition
# ---------------------------------------------------------------------------------------- #

class GUIState(enum.Enum):
    NONE = enum.auto()
    START = enum.auto()
    COHORT_SELECT = enum.auto()
    COHORT_SETUP = enum.auto()
    COHORT_EDIT = enum.auto()
