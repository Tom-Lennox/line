# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

# get a font
#   This example is for Windows (7, etc.).
#   If you use Unix-like system, fonts are found at
#   for example "/usr/share/fonts".
fnt = ImageFont.truetype('c:/Windows/Fonts/msmincho.ttc', 150)
# fnt = ImageFont.truetype('msmincho.ttc', 30)

img = Image.open("1.jpg")  # open base image
dctx = ImageDraw.Draw(img)  # create drawing context

# text to draw
txt = u"LGTM"  # Tokyo tower and San'en-zan Zōjō-ji

# calculate text size
txtsz = dctx.textsize(txt, fnt)

# draw text
dctx.text(
    # draw text at near (right, top)
    (img.width - txtsz[0] - 20, 20),
    txt,
    font=fnt,
    fill="#eeeeff"
    )

del dctx  # destroy drawing context

img.save("ImageDraw_text_01.jpg")
