#!/usr/bin/env python
# -*- coding：utf-8 -*-
from __future__ import print_function

import os
import sys

from PIL import Image, ImageEnhance

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = os.path.splitext(infile)[0] + ".point.png"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                enh = ImageEnhance.Contrast(im)
                enh.enhance(1.3).show("30% more contrast")
        except IOError:
            print("cannot convert", infile)
