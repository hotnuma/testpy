#!/usr/bin/env python3

import os
import sys

n = len(sys.argv)

if n != 2:
    print("No input directory")
    sys.exit(1)
   
folder = sys.argv[1]

if not os.path.isdir(folder):
    print("error")
    sys.exit(1)

for root, dirs, files in os.walk(folder):
    for fname in files:
        print(root)
        print(fname)
        print("")
        
