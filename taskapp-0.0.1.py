#!/usr/bin/python
import os
import sys
import json
import datetime
import re

HomeDir = os.environ["HOME"]
dataLoc = HomeDir + "/NextCloud/Todo"


# load todos
def readTodo():
    with open(f"{dataLoc}/todo.json", 'r') as f:
        try:
            data = json.load(f)
        except:
            data = None
    return data


# date Parse
def dateparse(inp):
    days = {
        0: ('monday', 'mon'),
        1: ('tuesday', 'tues'),
        2: ('wednesday', 'wed'),
        3: ('thursday', 'thurs'),
        4: ('friday', 'fri'),
        5: ('saturday', 'sat'),
        6: ('sunday', 'sun')
    }



    inp = inp.strip()
    if re.match("\\d{1,2}/\\d{1,2}/\\d{1,2}", inp):
        due = inp.split('/')
        due[2] = f"20{due[2]}"
        for i in range(3):
            due[i] = int(due[i])

        due = datetime.date(due[2], due[1], due[0])
        return False, due
    else:
        return True, 'Date not Recognised'
    # due = datetime.date(input)


# print list
def printList():
    pass


# COMMANDS ----------------------------

# help command
def help(args=[]):
    if args:
        pass
    else:
        print('none')


# add command
def add(args=None):
    task = input('Title: ')

    due = input('Due: ')
    error, response = dateparse(due)
    if error:
        print(response + '\n')
        return
    else:
        print(response)

    diff = input('Difficulty: ')


# END COMMANDS ------------------------


# commands
commands = {
    'a': add,
    'h': help
}

run = True
#  main loop
while run is True:
    #    os.system('\clear')
    todoData = readTodo()
    printList()

    command = input("Command~> ")
    command.strip()
    if ' ' in command:
        command = command.split(' ')
        commands[command[0]](command[1:])
    else:
        try:
            commands[command]()
        except KeyError as e:
            print(f'{e} is not a command\n'
                  f'try h for help\n')
