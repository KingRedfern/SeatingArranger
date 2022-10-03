""" person.py - Base class for cohort members and teachers """

class Person:

    def __init__(self, personal: str, family: str):
        self.personal_name: str = personal
        self.family_name: str = family

    # ------------------------------------ GETTER METHODS ------------------------------------ #

    def get_given_name(self):
        return self.personal_name

    def get_family_name(self):
        return self.family_name

    # ------------------------------------ SETTER METHODS ------------------------------------ #

    def change_personal_name(self, new_personal_name):
        self.personal_name = new_personal_name
        return

    def change_family_name(self, new_family_name):
        self.family_name = new_family_name
        return
