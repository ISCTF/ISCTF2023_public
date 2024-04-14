#!/bin/sh
mkdir /task
python3 /task.py
rm -rf /task
mkdir /task
mv /flag.zip /task/flag.zip
cd task && python3 -m http.server
