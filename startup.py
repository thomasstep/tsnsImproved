#!/usr/bin/python

import subprocess
import sys

#subprocess.call(["gnome-terminal", "-c python /home/csce438/test.py"], shell=True)

subprocess.Popen(["gnome-terminal", "-x", "/home/csce438/tsnsImproved/tsd", "-p "+sys.argv[1]])
