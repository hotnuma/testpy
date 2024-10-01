#!/usr/bin/env python3

import os, sys
import subprocess

def runcmd(cmd):
    ret = subprocess.run(cmd, shell=True, capture_output=True)
    result = ret.stdout.decode()
    return result

def main():
    cmd = "ls -la"
    result = runcmd(cmd)
    if result == "":
        print("an error occured...")
        return 1
    print(result)
    return 0

if __name__ == "__main__":
    main()


