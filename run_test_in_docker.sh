#!/bin/sh

virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python test.py
