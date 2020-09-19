# 【参考】http://satemochi.blog.fc2.com/blog-entry-95.html

# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGBA', (1500, 900))
draw = ImageDraw.Draw(img)
# draw.font = ImageFont.truetype('~/Library/Fonts/keifont.ttf', 200)
draw.font = ImageFont.truetype('~/meiryo.ttc', 300)
text = u'LGTM'

pos = (np.array(img.size) - np.array(draw.font.getsize(text))) / 2.
print(np.array(img.size))
print(draw.font.getsize(text))
print(np.array(draw.font.getsize(text)))
print(np.array(pos))

bw = 6

fontColor = '#ffffff'
edgeColor = '#000000'

draw.text(pos-(-bw, -bw), text, edgeColor)
draw.text(pos-(-bw, +bw), text, edgeColor)
draw.text(pos-(+bw, -bw), text, edgeColor)
draw.text(pos-(+bw, +bw), text, edgeColor)
draw.text(pos, text, fontColor)

img = img.resize((500, 300), Image.ANTIALIAS)
img.save('j1.png')
img.show()


# # -*- coding: utf-8 -*-
# import os.path
# from matplotlib import pyplot as plt
# from matplotlib import patheffects as path_effects
# from matplotlib.font_manager import FontProperties
 
 
# fig = plt.figure(facecolor=(0.75, 0.75, 0.75))
# # fp = FontProperties(fname=os.path.expanduser('~/Library/Fonts/keifont.ttf'))
# fp = FontProperties(fname=os.path.expanduser('c:/Windows/Fonts/msmincho.ttc'))

# txt = plt.gcf().text(0.5, 0.5, u'LGTM', color='red',
#                                ha='center', va='center', size=60,
#                                fontproperties=fp)
# txt.set_path_effects([path_effects.Stroke(linewidth=10, foreground='yellow'),
#                       path_effects.Normal()])
# plt.savefig('j2.png', bbox_inches='tight', facecolor=fig.get_facecolor(),
#             transparent=True)
# plt.show()