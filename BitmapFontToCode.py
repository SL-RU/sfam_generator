import PIL
from PIL import Image, ImageFont, ImageDraw
from cp1251 import *
from config import *
import math

im = Image.open(bitmap_png)


s = "uint8_t font[] = {\n"

bytesinchar = 0

def print_char(x, y):
	global default_h, default_w, im, bytesinchar
	i = 0
	sg = ""
	bits = list()
	for i in range((default_h + 1) * default_w):
		if(i%8 == 0 and i != 0):
			bits.append(sg)
			sg = ""
		r,g,b = im.getpixel((x + i%default_w, y + i/default_w))
		sg += '1' if (r == g == b == 255) else '0'
	# print(i)
	if i%8 != 0 and i%8 != 7:
		while i%8 != 0:
			i += 1
			sg += "0"
		bits.append(sg)

	out = ""
	bytesinchar = 0
	for z in bits:
		if(hexorbit == "hex"):
			out += ("0x%02x" % int(z[::-1], 2)) + ", "
		else:
			out += "0b" + z[::-1] + ", "
		bytesinchar += 1
		#print(out)
	return out

y = 3
x = 1
for i in range(start_char_num, cp_count):
	s += print_char(x, y) + "\n"
	x += default_w + 1
s+="};"

if(output_file != ""):
	with open(output_file, "w") as fl:
		fl.write(s)
print(s)
print("Byte width: " + str(bytesinchar))