import os
import sys

path = os.path.dirname(__file__)
dirs = os.listdir(path)

for file in dirs:
    print(file)
    
   