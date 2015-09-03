#!/usr/bin/env python
import subprocess

jobs = range(1, 50)

for i in jobs:
    p = subprocess.Popen(['python', 'test.py', str(i)])

raw_input('Press any key to exit...')
