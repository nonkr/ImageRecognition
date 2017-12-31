#!/usr/bin/env python
# -*- coding：utf-8 -*-
from __future__ import print_function

import sys

from PIL import Image

if __name__ == "__main__":
    infile = sys.argv[1]
    try:
        with Image.open(infile) as im:
            print("original =", im.mode, im.size)
            im.draft("L", (100, 100))
            print("draft =", im.mode, im.size)
    except IOError:
        print("cannot convert", infile)
