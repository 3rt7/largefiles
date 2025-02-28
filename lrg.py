#!/usr/bin/python3

import os
from pathlib import Path as pth
import sys

USAGE = '''
Print files or directories larger than specified size

Usage: ./main.py <path> <size>

<path> - search <path>
<size> - print files or folders larger than <size> (in Mb)

Written by Erfan zamani <erfanzm99@gmail.com>
'''

try:
    dir_to_search = sys.argv[1]
    size_to_look = int(sys.argv[2])
except:
    print(USAGE)
    sys.exit(1)

dest = pth(dir_to_search)
totalsize = 0
for dir, sub, files in dest.walk():
    parentdir = dir
    for file in files:
        fullpath = dir / file
        if not fullpath.is_file():
            continue

        filesize = round(os.path.getsize(fullpath) / 1000000) # convert to MB
        if (filesize > size_to_look):
            print(f"size of file {fullpath} is {filesize}Mb")
        totalsize += filesize

    if totalsize > size_to_look:
        print(f"size of directory {parentdir} is {totalsize}Mb")
        totalsize = 0

