#!/usr/bin/env python3

import sys
import os
import subprocess

def runcmd(cmd):
    ret = subprocess.run(cmd, shell=True, capture_output=True)
    result = ret.stdout.decode()

    if result == "":
        print("error")
        return 1
    
    print(result)
    
    return 0

def main():
    cmd = "ls -la"
    
    runcmd(cmd)
    
    return 0

if __name__ == "__main__":
    main()


