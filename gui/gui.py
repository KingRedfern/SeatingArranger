""" gui.py - Class for the GUI's handler """

import PySimpleGUI as gui
from typing import Union

from definitions import CURRENT_VERSION, COHORT_REGISTER_PATH, NEXT_BUTTON_TEXT
from cohort.cohort import Cohort
from utils.json_utils import read_from_json_file
from utils.gui_utils import GUIState

# ---------------------------------------------------------------------------------------- #
# Constants
# ---------------------------------------------------------------------------------------- #

GUI_THEME = gui.theme_global('DarkAmber')


# ---------------------------------------------------------------------------------------- #
# Class definition
# ---------------------------------------------------------------------------------------- #

class GUI:
    """ """

    def __init__(self):

        self.window: gui.Window = None
        self.title = f"Seating Arranger v.{CURRENT_VERSION}"
        self.state: GUIState = GUIState.NONE

        self.cohort_name: str = ""
        self.cohort = None

        return

    # ---------------------------------------------------------------------------------------- #

    def gui_service(self):
        """ """
        while True:
            try:
                if self.state is GUIState.NONE:
                    pass
                elif self.state is GUIState.START:
                    pass
                elif self.state is GUIState.COHORT_SELECT:
                    self.window_select_cohort()
                elif self.state is GUIState.COHORT_SETUP:
                    self.window_set_up_cohort()
                elif self.state is GUIState.COHORT_EDIT:
                    pass
                else:
                    pass

            except Exception as err:
                self.window_error(err=err)
                break

        LAYOUT = [[gui.Text('Welcome to the seating arranger.')],
                  [gui.Text('Enter something on Row 2'), gui.InputText()],
                  [gui.Button('Ok'), gui.Button('Cancel')]]

        # EXTANT COHORT
        num_stu_per_table = int(input(f"How many tables do you want to sort students into?"))
        print(f"How many seating arrangements for tables of {num_stu_per_table} students would you like to generate?")
        print(f"How strict should the sorting be?")
        print(f"Sit students anywhere\n"
              f"Don't sit students next to people they've already sat next to\n"
              f"Don't sit students at the same table as people they've already sat next to")

        return

    # ------------------------------------ RUNNER METHODS ------------------------------------ #

    def _run_window(self, layout: Union[list, tuple], close_events: list = [NEXT_BUTTON_TEXT]):
        """

        Args:
            layout (list, tuple):
            close_events:

        Returns:
            event:
            values[0]:
        """
        if self.window is not None:
            if not self.window.is_closed:
                self.window.close()

        self.window = gui.Window(title=self.title, layout=layout)
        while True:
            event, values = self.window.read()
            if event == gui.WINDOW_CLOSED or event in close_events:
                # The user closes the window or hits a button to close the window
                break

        self.window.close()
        self.window = None

        return event, values[0]

    # ---------------------------------- FSM STATES METHODS ---------------------------------- #

    def window_select_cohort(self):
        """ """
        buttons = ['NEW COHORT']
        cohort_list = read_from_json_file(COHORT_REGISTER_PATH)
        for cohort in cohort_list['cohorts']:
            buttons.append(cohort)

        layout = [[gui.Text('Please select a cohort:')],
                  [gui.Radio(button, 1) for button in buttons],
                  [gui.Button(NEXT_BUTTON_TEXT)]]
        self.cohort_name = self._run_window(layout)[0]
        self.state = GUIState.COHORT_SETUP
        return

    def window_set_up_cohort(self):
        """ """
        layout = []
        if self.cohort_name is 'NEW COHORT':
            # Choose an input method
            layout.append([gui.Text("To add members to a new cohort, you can manually input names, or have the names "
                                    "read from a .csv file. Which would you prefer?")])
            layout.append([gui.Button("Manual Input"), gui.Button(".csv File")])
            layout.append([gui.Text("Please note that you can add and remove members from a cohort later, and update "
                                    "the names of cohort members.")])
            event = self._run_window(layout=layout, close_events=["Manual Input", ".csv File"])[0]

            if event == "Manual Input":
                pass
                # members have numbers
            elif event == ".csv File":
                # names from .csv
                print(f"Please input the name of the column containing family names: ")
                print(f"Please input the name of the column containing given names: ")
                print(f"Please input the absolute filepath to the .csv file with the list of names. \nC:")

            # Get the new cohort's name
            layout.append([gui.Text("Please input the name of the new cohort: "), gui.InputText(tooltip="Enter the "
                                                                                                        "new cohort's "
                                                                                                        "name here")])
            layout.append([gui.Button(NEXT_BUTTON_TEXT)])
            self._run_window(layout=layout)

            # add the cohort to a .json file
            # add the cohort to the cohort register

            self.cohort = Cohort(self.cohort_name)
        else:

            # Load cohort from .json file
            pass

        return

    def window_error(self, err):
        """ """
        if not self.window.is_closed:
            self.window.close()

        title = "Error"
        layout = [gui.Text("There was an error running the program."),
                  gui.Text(err),
                  gui.Text("Shutting down the program..."),
                  gui.CloseButton("Okay")]

        self._run_window(layout=layout)
        return
