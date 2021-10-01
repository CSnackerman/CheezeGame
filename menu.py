from buttons import CenteredRoundedButton, ExitButton
from utility import *

class Menu:

    


    def __init__ (self):

        button_width = pcToPx_horiz (15)
        button_height = pcToPx_vert (7)
        button_radius = pcToPx_vert (5) 
        start_button_y = pcToPx_vert (70)
        settings_button_y = pcToPx_vert (85)

        self.buttons = {
            'start':    CenteredRoundedButton (
                            button_radius, 
                            'START', 
                            0, 
                            start_button_y, 
                            button_width, 
                            button_height
                        ),

            'settings': CenteredRoundedButton (
                            button_radius, 
                            'SETTINGS', 
                            0, 
                            settings_button_y, 
                            button_width, 
                            button_height
                        ),

            'exit':     ExitButton (
                            '',
                            100, 100,
                            25,
                            '#FFFFFF', '#000000'
                        )
        }

    
    def display (self, win_surf):

        for key in self.buttons:
            self.buttons[key].draw (win_surf)