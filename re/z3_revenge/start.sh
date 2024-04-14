#!/bin/sh
python3 z3_revenge.py
mkdir /task
gcc /z3_revenge.c -o /task/z3_revenge
cd /task && python3 -m http.server