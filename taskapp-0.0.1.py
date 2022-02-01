#!/usr/bin/python
import os
import sys
import json

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


# print list
def printList():
    pass


run = True
#  main loop
while run is True:
    os.system('\clear')
    todoData = readTodo()
    printList()

