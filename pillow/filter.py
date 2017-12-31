#!/usr/bin/env python
# -*- coding：utf-8 -*-
from __future__ import print_function

import os
import sys

from PIL import Image, ImageFilter

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = os.path.splitext(infile)[0] + ".filter.png"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im = im.filter(ImageFilter.DETAIL)
                im.save(outfile)
        except IOError:
            print("cannot convert", infile)
