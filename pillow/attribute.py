#!/usr/bin/env python
# -*- coding：utf-8 -*-
from __future__ import print_function

import sys

from PIL import Image

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, "%dx%d" % im.size, im.mode, im.getbands())
    except IOError:
        pass
