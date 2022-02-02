#!/usr/bin/python
import os
import sys
import json

HomeDir = os.environ["HOME"]
dataLoc = HomeDir + "NextCloud/Todo"


# load todos
def readTodo():
    with open(f"{dataLoc}/todo.json", 'r') as f:
        try:
            data = json.load(f)
        except:
            data = None
    return data


# print list
def printList():
    pass

# help command
def help(args=[]):
    if args:
        pass
    else:
        print('none')

# add command
def add(args=[]):
    task = input('Title: ')
    due = input('Due: ')
    diff = input('Difficulty: ')



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
        commands[command]()
