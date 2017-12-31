#!/usr/bin/env python
# -*- coding：utf-8 -*-
from __future__ import print_function

import os
import sys

from PIL import Image

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = os.path.splitext(infile)[0] + ".merge.png"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                r, g, b, a = im.split()
                im = Image.merge("RGB", (b, g, r))
                im.save(outfile)
        except IOError:
            print("cannot convert", infile)
