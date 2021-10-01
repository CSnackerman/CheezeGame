from buttons import CenteredRoundedTextButton, ExitButton
from utility import *
from events import EventHandler

class Menu:

    def __init__ (self):

        button_width = pcToPx_horiz (15)
        button_height = pcToPx_vert (7)
        rounded_radius = pcToPx_vert (5) 
        start_button_y = pcToPx_vert (70)
        settings_button_y = pcToPx_vert (85)

        self.buttons = {
            'start':    CenteredRoundedTextButton (
                            'START',
                            0, start_button_y,
                            button_width, button_height, rounded_radius,
                            '#FFFFFF', '#000000'
                        ),

            'settings': CenteredRoundedTextButton (
                            'SETTINGS',
                            0, settings_button_y,
                            button_width, button_height, rounded_radius,
                            '#FFFFFF', '#000000'
                        ),

            'exit':     ExitButton (
                            WIDTH - 100, 50,
                            25,
                            '#FFFFFF', '#000000'
                        )
        }

        # add listeners
        self.buttons ['start'].addClickListener (Menu.clickStartCallback)
        self.buttons ['settings'].addClickListener (Menu.clickSettingsCallback)
        self.buttons ['exit'].addClickListener (Menu.clickExitCallback)


    def display (self, win_surf):
        for key in self.buttons:
            self.buttons[key].draw (win_surf)
    

    # listener callbacks
    def clickStartCallback ():
        print ('clicked start')

    def clickSettingsCallback():
        print ('clicked settings')

    def clickExitCallback():
        EventHandler.postQuit()


    
    