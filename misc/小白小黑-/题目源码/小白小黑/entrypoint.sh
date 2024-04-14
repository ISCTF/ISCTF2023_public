#!/bin/sh
mkdir /task
python3 /task.py
cd task && python3 -m http.server