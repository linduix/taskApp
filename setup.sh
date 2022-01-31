#!/bin/bash

pip install -r ./requirements.txt

cd  $HOME/.local/share/
mkdir todoapp
touch todoapp/todo.json
