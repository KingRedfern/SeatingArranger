"""
cohort_base.py - Base class for handling I/O for Cohort objects
"""

from definitions import COHORT_REGISTER_PATH, NEXT_BUTTON_TEXT
from people.member import Member
from utils.json_utils import read_from_json_file, get_path_to_cohort_json_file, update_cohort_register


# ---------------------------------------------------------------------------------------- #
# Class definition
# ---------------------------------------------------------------------------------------- #

class BaseCohort:

    def __init__(self, name: str, **kwargs):
        self.name: str = name
        self.filepath = get_path_to_cohort_json_file(cohort=self.name)
        self.cohort: list = []
        if 'cohort' in kwargs:
            self.cohort = kwargs['cohort']

        self.arrangements: dict = {}

        self._in_directory: bool = False

        self._parse_cohort()

        return

    def _parse_cohort(self):
        if self._check_cohort_in_directory():
            self.cohort = read_from_json_file(self.filepath) # This gives a list of people names and seating, need to parse it to students
        else:
            update_cohort_register(self.name)
            cohort_data = {}
            for stu in self.cohort:
                cohort_data.update(stu.)
            # Todo: Add Students to Cohort

        self._parse_arrangements()

        return

    def _check_cohort_in_directory(self) -> bool:
        cohort_directory = read_from_json_file(COHORT_REGISTER_PATH)
        if self.name in cohort_directory['cohorts']:
            return True
        else:
            return False

    def _parse_arrangements(self):
        pass

    def _add_student_to_cohort(self, given: str, family: str):
        newbie = Member(given=given, family=family)
        self.cohort.append(newbie)
        return

