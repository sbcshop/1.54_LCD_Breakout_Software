#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from Library import lcd_lib
from PIL import Image,ImageDraw,ImageFont

RST = 27
DC = 25
BL = 18

disp = lcd_lib.LCD(spi_freq=40000000,rst=RST,dc=DC,bl=BL)
disp.Init() # Initialize library.
disp.clear_display() # Clear display.

img = Image.open('../pic/img.jpg')	
img_rotate=img.rotate(90)
disp.show_img(img_rotate)

time.sleep(400)

img1 = Image.new("RGB", (disp.width, disp.height), "WHITE")
draw = ImageDraw.Draw(img1)

Font1 = ImageFont.truetype("../Font/Font01.ttf",25)
Font2 = ImageFont.truetype("../Font/Font00.ttf",28)

draw.text((5, 10), 'SB COMPONENTS', fill = "BLUE",font=Font2)
draw.text((5, 80), '1.54 LCD', fill = "RED",font=Font2)
draw.text((5, 130), 'BREAKOUT', fill = "BLACK",font=Font2)

img1_rotate=img1.rotate(90)
disp.show_img(img1_rotate)

time.sleep(2)
disp.exit()
  


