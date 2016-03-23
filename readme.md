#Simple Font And Image generator

Simple scripts for generating bit fonts for STM32, AVR, Arduino or other MCU, game and etc.

#How to use Font Generator

1) Install python 3.4 or newer

2) Install [PILLOW](http://python-pillow.org/):

```Bash
pip install Pillow
```

3) Select font and place it in the folder with scripts

4) Edit config.py

5) run GenerateFontBitmap.py, it will be create and open image with name as bitmap_png value:

```
python GenerateFontBitmap.py
```

6) Check and edit bitmap_png. Regenerate font if thats required.

Check this:

* All chars must be in their cells
* If cell is blue, that means it's height more then default and it was offseted up.
* Check if white pixels isn't on cell outline. Like this ![alt text](https://raw.githubusercontent.com/SL-RU/sfam_generator/master/screenshots/bad.png)

If something wrong you can change anything in any image editor.

Good font must be look like:
![](https://raw.githubusercontent.com/SL-RU/sfam_generator/master/screenshots/normal.png)

7) Generate code with:
```
python BitmapFontToCode.py
```

8) DONE! Use this font wherever you want! For example:
![](https://raw.githubusercontent.com/SL-RU/sfam_generator/master/screenshots/cons1.png)
![](https://raw.githubusercontent.com/SL-RU/sfam_generator/master/screenshots/cons2.png)

#How to use Image generator:

1) Edit "png" value in ImageToCode.py. That is a path to image.

2) Generate code and file:
```
python ImageToCode.py
```
You can find usage of generated code here: https://github.com/SL-RU/stm32libs/blob/master/HAL/ssd1306/ssd1306.c in function void ssd1306_image(uint8_t *img, uint8_t x, uint8_t y)

Video: http://www.youtube.com/watch?v=g6N0J6xSCS0

#How to use font with [my ssd1306 stm32 library](https://github.com/SL-RU/stm32libs/tree/master/HAL/ssd1306):

1) Add defenition in fonts.h
![](https://raw.githubusercontent.com/SL-RU/sfam_generator/master/screenshots/keil2.png)

2) Add generated font data to fonts.c and set params
```
const uint8_t customfont[] = {
  //output_file text
};
FontDef_t custom_font = {
	width,
	height,
	byte width, //in the end of output BitmapFontToCode.py
	customfont
};
```
![](https://raw.githubusercontent.com/SL-RU/sfam_generator/master/screenshots/keil1.png)

Good luck!
