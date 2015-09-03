#!/usr/bin/env python

import fcntl
import os
import sys

job_id = sys.argv[1]
basedir = '/tmp/lslock-test'
dirname = '%s/%s' % (basedir, job_id)
filename = '%s/%s.lock' % (dirname, job_id)

try:
    os.makedirs(dirname)
except: pass

# Lock file
f = open(filename, 'w')
fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)

# Wait input
raw_input()
