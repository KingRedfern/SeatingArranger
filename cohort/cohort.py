"""
cohort.py - Class for representing a cohort of students
"""

from cohort_base import BaseCohort


# ---------------------------------------------------------------------------------------- #
# Class definition
# ---------------------------------------------------------------------------------------- #

class Cohort(BaseCohort):

    def __init__(self, name: str, **kwargs):
        """ """
        super().__init__(name, **kwargs)
        return
