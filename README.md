==========================
About    
==========================
Author:			Roman Zaikin

This project shows you an interesting way to hide executable inside an image using bits to pixel.
The file you want to hide inside the image will be parsed to binary 0 and 1, then it will be placed into colors with the following logic:
```
0 –	 (0,255,0) 	GREEN
1 –	 (255,0,0)	RED
```
![alt tag](https://github.com/romanzaikin/PEImage/blob/master/Test.png)

==========================
Description
==========================

<b>Put exe into Image:</b>

note: the file "Test.png" will be the name of the new created file.
```
engine = PEImage("Test.png","sleeptest.exe")
engine.FileToImage()
```
<b>Get the exe from the image</b>

note: you will be prompt for the file name input.
```
engine = PEImage("Test.png")
engine.ImageToFile()
```
