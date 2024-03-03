import os

path = r'/Users/kerimkular/Desktop/pp2-22B050847/tsis6/dirandfiles'
if os.path.exists(path):
   print("Yes")
   filename = os.path.split(path)
   print(filename)
   print(filename[0])
   print(filename[1])
else:
   print("path is not exist")