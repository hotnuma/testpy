#!/usr/bin/env python3
import os, sys

args = sys.argv
size = len(args)
if size < 2: exit(1)

opt_val = ""
i = 1
while i < size:
    if args[i] == "-opt":
        i += 1
        if i >= size: exit(1)
        opt_val = args[i]
    else:
        exit(1)
    i += 1

print(opt_val)

