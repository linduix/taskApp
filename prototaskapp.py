import sys, os
from pynput import keyboard
from classes import cursor, printc


class app(object):
    def __init__(self):

        self.pages = {
            1: 'home'
        }
        self.cursor = cursor()
        self.printc = printc()

        # ----------------------------------------------------

        try:
            self.colms = os.get_terminal_size().columns
        except OSError as e:
            self.printc.red(f'{e}: Terminal not recognised')
            sys.exit(1)

        self.main()

    def main(self):

        run = True
        while run:
            inp = input('>> ')
            if inp.strip() == 'a':
                self.add()

    @staticmethod
    def add():
        question = '[\033[33m?\033[0m] '

        print(question + 'Title: ')
        title = sys.stdin.readline()

        print(title)

        pass


if __name__ == '__main__':
    app = app()
