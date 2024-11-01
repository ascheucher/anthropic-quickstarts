#!/bin/bash

set -e

cd $HOME/PyAutoGUIControl
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  source .venv/bin/activate  
  pip install --upgrade pip
  pip install -r requirements.txt
else
  source .venv/bin/activate
fi

DISPLAY=:1 python3 push_the_mouse.py