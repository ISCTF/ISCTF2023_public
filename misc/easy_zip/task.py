# -*- coding: utf-8 -*-
import os
import random
pwd = str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
os.system('zip -q -r -j -P '+pwd+' /flag.zip /task/flag')

