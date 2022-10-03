"""
people.py - Class for representing members of a cohort
"""

from person import Person


# ---------------------------------------------------------------------------------------- #
# Class definition
# ---------------------------------------------------------------------------------------- #

class Member(Person):

    def __init__(self, given: str, family: str, seat_history=None):
        super().__init__(given, family)
        self.id_no: int = 0
        self.seat_history: dict = seat_history
        return

    # ------------------------------------ GETTER METHODS ------------------------------------ #

    def get_seating_history(self):
        return self.seat_history

    # ------------------------------------ SETTER METHODS ------------------------------------ #

    def sit_next_to(self):
        self.seat_history
