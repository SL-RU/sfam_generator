#Simpl Font And Image generator

Simple scripts for generating bit fonts for STM32, AVR, Arduino or other MCU, game and etc.

#How to use

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
* Check if white pixels isn't on cell outline 

If something wrong you can change anything in any image editor.

Good font must be look like:


7) Generate code with:
```
python BitmapFontToCode.py
```

8) DONE! Use this font wherever you want! For example:

#How to use it with [my ssd1306 stm32 library](https://github.com/SL-RU/stm32libs/tree/master/HAL/ssd1306):

