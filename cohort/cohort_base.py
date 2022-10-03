"""
cohort_base.py - Base class for handling I/O for Cohort objects
"""

from definitions import COHORT_DIRECTORY_PATH
from student.student import Student
from utils.io_utils import read_from_json_file

class BaseCohort:

    def __init__(self, source):
        self.source = source
        self.cohort: list = []
        self.arrangements: dict = {}

        return

    def _read_cohort_directory(self):
        cohort_directory = read_from_json_file(COHORT_DIRECTORY_PATH)


    def _add_student(self, given: str, family: str):
        newbie = Student(given=given, family=family)
        self.cohort.append(newbie)
        return

