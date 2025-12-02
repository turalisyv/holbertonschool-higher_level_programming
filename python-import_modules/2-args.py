#!/usr/bin/python3

import sys

for i in range(len(sys.argv) - 1):
    print("{}: {}".format(i+1, sys.argv[i+1]))
