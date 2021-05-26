#!/usr/bin/env bash

VENVNAME=venv

python -m venv $VENVNAME
source $VENVNAME/Scripts/activate
python ../get-pip.py

test -f requirements.txt && pip install -r requirements.txt

echo "build $VENVNAME"