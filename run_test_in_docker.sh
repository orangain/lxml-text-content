#!/bin/sh

virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
dpkg -l | grep libxml2
python test.py
