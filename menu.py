from buttons import Button, CenteredButton, CenteredRoundedButton

class Menu:

    def __init__ (self):
        self.buttons = {
            'default' : Button(),
            'start'  :   CenteredButton (y=100, text_val='START', w=100, h=50),
            'settings': CenteredRoundedButton (25, 'SETTINGS', 0, 200, 100, 50)
        }

    
    def display (self, win_surf):

        for key in self.buttons:
            self.buttons[key].draw (win_surf)