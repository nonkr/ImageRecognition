#!/usr/bin/env python
# -*- coding：utf-8 -*-
from __future__ import print_function

import os
import sys

from PIL import Image

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = os.path.splitext(infile)[0] + ".transpose.png"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                # im = im.resize((128, 128))
                # im = im.rotate(45)
                # im = im.transpose(Image.FLIP_LEFT_RIGHT)
                # im = im.transpose(Image.FLIP_TOP_BOTTOM)
                # im = im.transpose(Image.ROTATE_90)
                im = im.transpose(Image.ROTATE_180)
                # im = im.transpose(Image.ROTATE_270)
                im.save(outfile)
        except IOError:
            print("cannot convert", infile)
