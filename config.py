default_w = 7 #width
default_h = 10 #height
cp_count = 256 #count of chars
start_char_num = 0 #first character id

#set encoding. You can find required encoding here: http://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/ and create own file like koi8.py or cp1251.py
def_encoding = "koi8"
#def_encoding = "cp1251"

font_path = "E:\\stm32\\sfam_generator/koi6x10.pil" #font path. You can use tft, otf or other supported by PILLOW libray: https://pillow.readthedocs.org/en/3.0.0/reference/ImageFont.html
#also you can use bdf or pcf (This way is better, because that fonts are pixel) simply run "pilfont blah.pcf" and .pil will be generated.
font_size = 10 #used only for truetype fonts

bitmap_png = "font.png" #output image


hexorbit = "hex" #set output format
#hexorbit = "bit" #set output format

output_file = "out.txt" #in this file will be printed generated code. You can set this var to "", then file won't be used.
