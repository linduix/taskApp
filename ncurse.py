# Draw text to center of screen
import curses
import os
from curses import wrapper

os.environ['TERM'] = 'alacritty'

class app(object):
    def __init__(self):

        ### init conf ####
        self.title = 'TASKS'
        self.screen = curses.initscr()

        ### color setup ###
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, 1, -1)
        curses.init_pair(2, 2, -1)
        curses.init_pair(3, 3, -1)

        red = curses.color_pair(1)
        green = curses.color_pair(2)
        yellow = curses.color_pair(3)

        self.colors = {
            'red': red,
            'green': green,
            'yellow': yellow
        }

        ### get size ###
        self.n_row, self.n_col = self.screen.getmaxyx()

        ### start mainloop in wrapper ###
        wrapper(self.main)

    def main(self, main_window):  # main func
        ### curses setup ###
        self.screen.keypad(1)
        curses.cbreak()
        curses.echo()

        ### pages ###
        pages = {
            0: None,  # quit
            1: self.drawDash()  # dashboard
        }

        ### mainLoop ###
        index = 1  # landing page
        while True:
            index = pages[index]

            # checking returnCode
            if not index:  # quit
                break

    def drawDash(self):
        win1 = curses.newwin(self.n_row - 4, self.n_col)

        win2 = curses.newwin(3, self.n_col, self.n_row - 3, 0)
        win2.keypad(1)


        # while True:
        ### win1 draw ###
        win1.border()
        win1.addstr(1, round(self.n_col / 2) - round(len(self.title) / 2),
                    self.title, self.colors['yellow'] | curses.A_BOLD | curses.A_UNDERLINE)

        ### win2 draw ###
        win2.border()
        win2.addstr(1, 1, '❯❯', self.colors['green'] | curses.A_BOLD)

        ### refresh ###
        win1.refresh()
        win2.refresh()

        ### get input ###
        x = win2.getstr(1, 4)

        ### clear ###
        win1.clear()
        win2.clear()

        ### pointer ###
        del win1
        del win2

        if x.decode() == 'q':
            return 0
        return 1


run = app()

# Convert the key to ASCII and print ordinal value
