#!/usr/bin/python
import os
import sys
import json

HomeDir = os.environ["HOME"]
with open(f"{HomeDir}/.local/share/todoapp/todo.json", 'r') as f:
    try:
        todoJson = json.load(f)
    except: 
        todoJson = None

print(todoJson)
