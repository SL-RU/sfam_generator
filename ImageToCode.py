import PIL
from PIL import Image, ImageFont, ImageDraw
import math, sys

#This script converts 1bit image to special byte file and code for using in your projects.
png = "pap.png" #Image file



out_f = png[:-4] + ".img"
print(out_f)

max_ll = 8

im = Image.open(png)

if im.width > 255 or im.height > 255:
	print("Image max width and heigh must be less then 256")
	sys.exit()

s = "uint8_t png[] = { " + str(im.width) + ", " + str(im.height) + ", //Width and height" 

i = 0
bits = list()
sg = ""
ou = ""
for i in range(im.width*im.height):
	if(i % im.width == 0):
		ou += ("\n")
	if i%8 == 0 and i != 0:
		bits.append(sg)
		sg = ""
	r,g,b = im.getpixel((i%im.width, i/im.width))
	if (r == g == b) and r > 100:
		ou += ("*")
	else:
		ou += (" ")
	sg += "1" if (r == g == b) and r > 100 else "0"

#print(ou)

if i%8 != 0 and i%8 != 7:
	while i%8 != 0:
		i += 1
		sg += "0"
	bits.append(sg)

i = 0
for b in bits:
	if i % max_ll == 0:
		s+="\n"
	i+=1
	s += ("0x%02x" % int(b[::-1], 2)) + ", "

s+= "\n};"

with open(out_f, "wb") as fl:
	fl.write(bytes([im.width, im.height]))
	fl.write(bytes(int(b[::-1], 2) for b in bits))


print(s)