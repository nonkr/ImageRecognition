#!/usr/bin/env python
from __future__ import print_function

import os
import sys

from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".crop.png"
    if infile != outfile:
        try:
            box = (100, 100, 400, 400)
            Image.open(infile).crop(box).save(outfile)
        except IOError:
            print("cannot convert", infile)
