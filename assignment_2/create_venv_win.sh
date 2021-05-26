#!/usr/bin/env bash

VENVNAME=venv

python -m venv $VENVNAME
source $VENVNAME/Scripts/activate
python ../get-pip.py

test -f requirements.txt && pip install -r requirements.txt

python -m spacy download en_core_web_sm

echo "build $VENVNAME"