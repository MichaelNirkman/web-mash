#!/bin/bash

# Web-Mash Launcher

# Variables
VENV_NAME='venv'

# Halt if URL was not supplied
if [ -z "$1" ]; then
    echo
    echo "No URL supplied!"
    echo
    exit 0
fi

# Install venv if not found yet
if [ ! -d ./$VENV_NAME ]; then
    echo 'Python venv was not found, creating'
    python3 -m venv $VENV_NAME
fi

source $VENV_NAME/bin/activate

python3 webmash.py $1