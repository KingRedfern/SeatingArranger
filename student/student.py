"""
student.py - Class for Person objects
"""


class Student:

    def __init__(self, given: str, family: str, seat_history=None):
        self.name: dict = {"given": given, "family": str}
        self.seat_history = seat_history
        return

    def print_name(self):
        return f"Given name  = {self.name['given']}\n" \
               f"Family name = {self.name['family']}"
