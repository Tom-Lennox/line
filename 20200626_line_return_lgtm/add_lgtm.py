# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

# def add_lgtm(src: str, desc: str) -> None:
# ||| C:\koko\line\20200626_line_return_lgtm\static\images\12218820163540.jpg
# ||| C:\static\images\12218820163540.jpg


# get a font
#   This example is for Windows (7, etc.).
#   If you use Unix-like system, fonts are found at
#   for example "/usr/share/fonts".

import numpy as np
# from PIL import Image, ImageDraw, ImageFont



# img = Image.new('RGBA', (1500, 900))
img = Image.open("./static/images/12218820163540.jpg")
draw = ImageDraw.Draw(img)

print(img.format, img.size, img.mode)
te = np.array(img.size)
print(te)
print(te[1] / 3)
width = te[1] / 3
print(int(width))

draw.font = ImageFont.truetype('~/meiryo.ttc', int(width))
text = u'LGTM'

pos = (np.array(img.size) - np.array(draw.font.getsize(text))) / 2.
bw = 1

fontColor = '#ffffff'
edgeColor = '#000000'

draw.text(pos-(-bw, -bw), text, edgeColor)
draw.text(pos-(-bw, +bw), text, edgeColor)
draw.text(pos-(+bw, -bw), text, edgeColor)
draw.text(pos-(+bw, +bw), text, edgeColor)
draw.text(pos, text, fontColor)

img = img.resize((500, 500), Image.ANTIALIAS)
img.save('j1.png')
img.show()
# img = img.resize((500, 300), Image.ANTIALIAS)
# img.save('j1.png')
# img.show()





# # calculate text size
# txtsz = dctx.textsize(txt, fnt)

# # draw text
# dctx.text(
#     # draw text at near (right, top)
#     (im.width - txtsz[0] - 20, 20),
#     txt,
#     font=fnt,
#     fill="#eeeeff"
#     )


# im.save("ImageDraw_text_01.jpg")


# import numpy as np
# from PIL import Image, ImageDraw, ImageFont

# img = Image.new('RGBA', (1500, 900))
# draw = ImageDraw.Draw(img)
# # draw.font = ImageFont.truetype('~/Library/Fonts/keifont.ttf', 200)
# draw.font = ImageFont.truetype('~/meiryo.ttc', 200)
# text = u'LGTM'

# pos = (np.array(img.size) - np.array(draw.font.getsize(text))) / 2.
# bw = 6
# draw.text(pos-(-bw, -bw), text, '#000000')
# draw.text(pos-(-bw, +bw), text, '#000000')
# draw.text(pos-(+bw, -bw), text, '#000000')
# draw.text(pos-(+bw, +bw), text, '#000000')
# draw.text(pos, text, '#ffffff')

# img = img.resize((500, 300), Image.ANTIALIAS)
# img.save('j1.png')
# img.show()