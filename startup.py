#!/usr/bin/python

import subprocess
import sys

subprocess.Popen(["gnome-terminal", "-x", "/home/csce438/tsnsImproved/tsd", "-p"+sys.argv[2], "-i"+sys.argv[1]])
