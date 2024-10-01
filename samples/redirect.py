#!/usr/bin/env python3

import os, sys
import subprocess

def runcmd(cmd):
    ret = subprocess.run(cmd, shell=True, capture_output=True)
    result = ret.stdout.decode()
    return (result, ret.returncode)

def main():
    cmd = "ls -la"
    result, ret = runcmd(cmd)
    if ret != 0:
        print("an error occured...")
        return ret
    print(result)
    return ret

if __name__ == "__main__":
    main()


