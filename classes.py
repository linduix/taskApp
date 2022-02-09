import datetime
import os
import sys

class cursor(object):
    @staticmethod
    def hide():
        sys.stdout.write('\x1b[?25l')

    @staticmethod
    def show():
        sys.stdout.write('\x1b[?25h')

    def up(self, n=None):
        if n:
            sys.stdout.write(f'\033[{n}A\r')
        else:
            sys.stdout.write(f'\033[A\r')

    def down(self, n=None):
        if n:
            sys.stdout.write(f'\033[{n}B\r')
        else:
            sys.stdout.write(f'\033[B\r')

    def right(self, n=None):
        if n:
            sys.stdout.write(f'\033[{n}C\r')
        else:
            sys.stdout.write(f'\033[C\r')

    def left(self, n=None):
        if n:
            sys.stdout.write(f'\033[{n}D\r')
        else:
            sys.stdout.write(f'\033[D\r')

    @staticmethod
    def clear():
        leng = os.get_terminal_size().columns
        sys.stdout.write('\r'+' '*leng+'\r')


class printc(object):
    def __init__(self):
        self.colors = {
            'foreground': '\033[0m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m'
        }

    def red(self, string):
        sys.stdout.write(f"{self.colors['red']}{string}{self.colors['foreground']}")

    def yellow(self, string):
        sys.stdout.write(f"{self.colors['yellow']}{string}{self.colors['foreground']}")

    def green(self, string):
        sys.stdout.write(f"{self.colors['green']}{string}{self.colors['foreground']}")


class task(object):
    def __init__(self, name, due):
        pass
