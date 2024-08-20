#!/usr/bin/env python3
# https://pynative.com/python-rename-file/

import sys
import os
import re

n = len(sys.argv)

if n != 2:
    print("No input directory")
    sys.exit(1)
   
folder = sys.argv[1]

if not os.path.isdir(folder):
    print("error")
    sys.exit(1)

for fname in sorted(os.listdir(folder)):
    path = os.path.join(folder, fname)
    print(path)


