# Draw text to center of screen
import curses
import os
from curses import wrapper

os.environ['TERM'] = 'alacritty'


def main(main_screen):
    screen = curses.initscr()
    screen.keypad(1)
    curses.cbreak()
    curses.echo()
    # curses.curs_set(0)

    curses.use_default_colors()
    curses.init_pair(1, 1, -1)
    red = curses.color_pair(1)

    n_row, n_col = screen.getmaxyx()

    title = 'TASKS'
    while True:
        win1 = curses.newwin(n_row - 3, n_col)
        win1.border()
        win1.addstr(2, round(n_col/2)-round(len(title)/2), title, red | curses.A_BOLD | curses.A_UNDERLINE)

        win2 = curses.newwin(1, n_col, n_row - 2, 0)
        win2.keypad(1)
        win2.addstr('❯❯')

        win1.refresh()
        win2.refresh()

        x = win2.getstr(0, 3)
        if x.decode() == 'q':
            return


wrapper(main)

# Convert the key to ASCII and print ordinal value
