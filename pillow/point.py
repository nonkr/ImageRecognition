#!/usr/bin/env python
# -*- coding：utf-8 -*-
from __future__ import print_function

import os
import sys

from PIL import Image

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = os.path.splitext(infile)[0] + ".point.png"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                # split the image into individual bands
                source = im.split()

                R, G, B = 0, 1, 2

                # select regions where red is less than 100
                mask = source[R].point(lambda i: i < 100 and 255)

                # process the green band
                out = source[G].point(lambda i: i * 0.7)

                # paste the processed band back, but only where red was < 100
                source[G].paste(out, None, mask)

                # build a new multiband image
                im = Image.merge(im.mode, source)

                im.save(outfile)
        except IOError:
            print("cannot convert", infile)
