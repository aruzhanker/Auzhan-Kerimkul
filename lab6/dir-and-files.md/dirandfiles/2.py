import os

path = r'/Users/kerimkularuzhan/Desktop/pp2-22B050847'
if os.path.exists(path):
    print("this file exists")
if os.access(path, os.R_OK):
    print("file is readable")
if os.access(path, os.W_OK):
    print("file is writeable")
if os.access(path, os.X_OK):
    print("file is executable")