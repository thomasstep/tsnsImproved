import subprocess

#subprocess.call(["gnome-terminal", "-c python /home/csce438/test.py"], shell=True)

subprocess.Popen(["gnome-terminal", "-x", "/usr/bin/python", "/home/csce438/test.py"])
