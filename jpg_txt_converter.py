#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
from bisect import bisect

img = Image.open('headphones_3.jpg')
pix = img.load()

file = open('headphones_txt', 'w')

signs = {0:' ', 1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:''}
bounds = [32, 64, 96, 128, 160, 192, 224]

width, height = img.size
print("Width :", width)
print("Height :", height)

index = bisect(bounds, 260)
print(index)
print(type(bounds))


brightnes = pix[3,4]
print(brightnes)
brightnes = 250 - brightnes[0]
print(brightnes)
#for i in range(height-1):
#    for j in range(width-1):
#        if i%2:
#            rgb = pix[j, i]
#            avgRGB = int(sum(rgb)/len(rgb))
#            if avgRGB < 145:
#                file.write(' ')
#            else:
#                file.write('#')
#    if i%2:
#        file.write('\n')


