#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
from bisect import bisect

img = Image.open('headphones.jpg')
pix = img.load()

file = open('headphones.txt', 'w')

signs = {0:'#', 1:'&', 2:'=', 3:'+', 4:'|', 5:':', 6:'.', 7:' '}
bounds = [32, 64, 96, 128, 164, 196, 224]

width, height = img.size
print("Width :", width)
print("Height :", height)

for i in range(height-1):
    for j in range(width-1):
        if i%2:
            rgb = pix[j, i]
            avgRGB = int(sum(rgb)/len(rgb))
            whichSign = bisect(bounds, avgRGB)
            file.write(signs[whichSign])
    if i%2:
        file.write('\n')


