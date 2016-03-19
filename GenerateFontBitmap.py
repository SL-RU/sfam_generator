import PIL
from PIL import Image, ImageFont, ImageDraw
from config import *
import cp1251, koi8




im = Image.new("RGB", ((default_w + 1) * (cp_count - start_char_num), default_h + 5))

dr = ImageDraw.Draw(im)

if(font_path.endswith(".pil")):
	fnt = ImageFont.load(font_path)
else:
	fnt = ImageFont.truetype(font_path, font_size)

s = ""

mw = 0
mh = 0
x = 0
y  = 3

def CHR(c):
	global def_encoding
	if(def_encoding == "koi8"):
		return chr(koi8.translate(cp1251.cp[i]))
	else:
		return chr(i)

print("St")
for i in range(start_char_num, cp_count):
	sz = fnt.getsize(CHR(i))
	if sz[0] > mw or sz[1] > mh:
		mw = max(mw, sz[0])
		mh = max(mh, sz[1])
		dr.point((x + 1, 0))
	if sz[1] > default_h:
		dr.rectangle([x, y-1, x + default_w, y + default_h], outline="Blue")
		cx =  x+ (default_w - sz[0])/2
		dr.text((cx + 1, y - sz[1] + default_h), CHR(i), font = fnt)
	else:
		dr.rectangle([x, y-1, x + default_w, y + default_h], outline="Red")
		cx = x+ (default_w - sz[0])/2
		dr.text((cx+1, y), CHR(i), font = fnt)
	x += default_w + 1

print("Max size: ", mw, " x ", mh)

for x in range(im.width):
	for y in range(im.height):
		r, g, b = im.getpixel((x, y))
		if ( r == g == b):
			if( r >100):
				dr.point((x, y), fill="White")
			else:
				dr.point((x, y), fill="Black")


im.show()
im.save(bitmap_png)