#!/usr/bin/env python3

import os
import sys


MAIN_MODULE = "__main__.py"


def getInput():
    sys.stdout.write("[*] Modes: search, spam\n")
    run = sys.stdin.read()
    return run

def getCdir():
    cdir = "."
    #dirs = __file__.split("/")[1:-1]
    #cdir = ""
    #for d in dirs:
    #    cdir = f"{cdir}/{d}"
    return cdir


def main():
    if len(sys.argv) != 2:
        main_module = MAIN_MODULE
    else:
        main_module = sys.argv[1]

    run = getInput()

    cdir = getCdir()
    
    cmd = f"source {cdir}/venv/bin/activate && source {cdir}/.env &&\
            python {cdir}/{main_module} {run}"
    os.system(cmd)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
