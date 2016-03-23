import PIL
from PIL import Image, ImageFont, ImageDraw
import math, sys

#This script converts 1bit image to special byte file and code for using in your projects.
png = "pinkie_pie_by_cellularsp-d4j7sj2.gif" #Image file


out_f = png[:-4] + ".img"
print(out_f)

max_ll = 8

im = Image.open(png)

if im.width > 255 or im.height > 255:
	print("Image max width and heigh must be less then 256")
	sys.exit()

s = ""
bits = list()

def frame_to_code(im, ext_bits):
	s = ""
	i = 0
	sg = ""
	ou = ""
	bits = list()
	for i in range(im.width*im.height):
		if(i % im.width == 0):
			ou += ("\n")
		if i%8 == 0 and i != 0:
			bits.append(sg)
			sg = ""
		rgb = im.getpixel((i%im.width, i/im.width))
		if rgb > 100:
			ou += ("*")
		else:
			ou += (" ")
		sg += "1" if rgb > 100 else "0"

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
	ext_bits.extend(bits)
	return (s, len(bits))

frame = 0
bits_len = 0

try:
	while 1:
		frame+=1
		ouu = im.convert("L")
		ouu = ouu.point(lambda x: 0 if x<128 else 255, '1')
		#ouu.save("out_gif" + str(frame) + ".png")
		sn, ln = frame_to_code(ouu, bits)
		s += "\n//Frame: " + str(frame - 1)
		s += sn
		bits_len = ln
		im.seek(im.tell()+1)
except EOFError:
	pass

s =  "uint8_t png[] = { " + str(im.width) + ", " + str(im.height) + ", " + str(frame) + ", " + str(bits_len & 0xFF) + ", " + str((bits_len >> 8) & 0xFF) + ", //Width, height, frame_count, frame_size_low_byte, frame_size_high_byte" + s + "\n};"
#print(frame)
with open(out_f, "wb") as fl:
	fl.write(bytes([im.width, im.height, frame, bits_len & 0xFF, (bits_len >> 8) & 0xFF]))
	fl.write(bytes(int(b[::-1], 2) for b in bits))

print(s)