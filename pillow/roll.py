#!/usr/bin/env python
# -*- coding：utf-8 -*-
from __future__ import print_function

import os
import sys

from PIL import Image


def roll(image, delta):
    "Roll an image sideways"

    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    part1.load()
    part2.load()
    image.paste(part2, (0, 0, xsize - delta, ysize))
    image.paste(part1, (xsize - delta, 0, xsize, ysize))

    return image


if __name__ == "__main__":
    infile = sys.argv[1]
    delta = int(sys.argv[2])
    outfile = os.path.splitext(infile)[0] + ".roll" + str(delta) + ".png"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                roll(im, delta).save(outfile)
        except IOError:
            print("cannot convert", infile)
