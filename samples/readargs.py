import os
import sys

args = sys.argv
size = len(args)
if size < 2:
    exit(1)

inpath = ""
i = 1
while i < size:
    part = args[i]
    if part == "-r":
        if i + 1 >= size:
            exit(1)
        i += 1
        inpath = args[i]
    elif i == 1:
        inpath = args[i]
    else:
        exit(1)
    i += 1

print(inpath)

