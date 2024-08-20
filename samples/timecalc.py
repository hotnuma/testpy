#!/usr/bin/env python3

# ffprobe -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 file.mp3

import sys
import os
import subprocess

def read_directory(folder):
    total = 0

    for fname in sorted(os.listdir(folder)):
        fullpath = os.path.join(folder, fname)
        total += get_duration(fullpath)

    total /= 60
    total = int(total)
    print(total)

def read_file(filepath):
    folder = os.path.dirname(filepath)
    fd = open(filepath, 'r')
    
    total = .0
     
    while True:
        line = fd.readline()
        if not line:
            break
        fname = line.strip()
        fullpath = os.path.join(folder, fname)
        total += get_duration(fullpath)
        print(fname)
     
    fd.close()

    total /= 60
    total = int(total)
    print(total)

def get_duration(filepath):
    cmd = "ffprobe -show_entries format=duration"
    cmd += " -of default=noprint_wrappers=1:nokey=1"
    cmd += " \"%s\"" % (filepath)

    ret = subprocess.run(cmd, shell=True, capture_output=True)
    result = ret.stdout.decode()
    val = .0

    if result == "":
        print("error")
        return .0

    val = float(result)
    return val

def main():
    n = len(sys.argv)

    if n != 2:
        print("No input directory")
        sys.exit(1)
       
    path = sys.argv[1]

    if os.path.isdir(path):
        read_directory(path)
        sys.exit(0)
    elif path.endswith(".m3u"):
        read_file(path)
        sys.exit(0)
    
    print("error")

if __name__ == "__main__":
    main()


