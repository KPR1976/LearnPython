#!/Users/KPR/pythonvirtual/bin/python -tt
import commands
import sys
import os


def List(dir):
    cmd = 'ls -l ' + dir
    (status, output) = commands.getstatusoutput(cmd)
    print output


def main():
    List(sys.argv[1])
