""" gui.py - Class for the GUI's handler """

import PySimpleGUI as gui
from typing import Union

from definitions import CURRENT_VERSION
from utils.gui_utils import GUIState

# ---------------------------------------------------------------------------------------#
# Constants
# ---------------------------------------------------------------------------------------#

GUI_THEME = gui.theme_global('DarkAmber')


# ---------------------------------------------------------------------------------------#
# Class definition
# ---------------------------------------------------------------------------------------#

class GUI:
    """ """

    def __init__(self):

        self.window: gui.Window = None
        self.title = f"Seating Arranger v.{CURRENT_VERSION}"
        self.gui_state: GUIState = GUIState.NONE

        return

    # ---------------------------------------------------------------------------------------#

    def gui_service(self):
        """ """
        while True:
            try:
                if self.gui_state is GUIState.NONE:
                    pass
                elif self.gui_state is GUIState.START:
                    pass
                elif self.gui_state is GUIState.SELECT_COHORT:
                    pass
                else:
                    pass

            except Exception as err:
                self.error_window(err=err)
                break

        LAYOUT = [[gui.Text('Welcome to the seating arranger.')],
                  [gui.Text('Enter something on Row 2'), gui.InputText()],
                  [gui.Button('Ok'), gui.Button('Cancel')]]
        print(f"Select the cohort you want to create a new seating for:")
        # top of the list is "NEW COHORT"

        # NEW COHORT
        print(f"To create a new cohort, you can manually input a list of first and last names, or have them read "
              f"from a .csv file. Which would you prefer?")

        print(f"Please input the name of the column containing family names: ")
        print(f"Please input the name of the column containing given names: ")
        print(f"Please input the absolute filepath to the .csv file with the list of names. \nC:")

        num_stu_per_table = int(input(f"How many tables do you want to sort students into?"))
        print(f"How many seating arrangements for tables of {num_stu_per_table} students would you like to generate?")
        print(f"How strict should the sorting be?")
        print(f"Sit students anywhere\n"
              f"Don't sit students next to people they've already sat next to\n"
              f"Don't sit students at the same table as people they've already sat next to")

        return

    def _run_window(self, layout: Union[list, tuple], close_events: list = None):
        """ """
        if self.window is not None:
            if not self.window.is_closed:
                self.window.close()

        self.window = gui.Window(title=title, layout=layout)
        while True:
            event, values = self.window.read()
            if event == gui.WINDOW_CLOSED or event in close_events:
                # The user closes the window or hits a button to close the window
                break

        self.window.close()
        self.window = None

        return values[0]

    def window_pick_a_cohort(self):
        """ """
        title = "Select the cohort you want to create a new seating for:"

    def error_window(self, err):
        """ """
        if not self.window.is_closed:
            self.window.close()

        title = "Error"
        layout = [gui.Text("There was an error running the program."),
                  gui.Text(err),
                  gui.Text("Shutting down the program..."),
                  gui.CloseButton("Okay")]

        self._run_window(title=title, layout=layout)
        return

