import binascii
import math
import os

from PIL import Image
from PIL import PngImagePlugin
from PIL import ImageFile

class PEImage(object):
    """
        Store and Retrieve PE file inside Image using pixel colors
        0   -   (255,0,0)
        1   -   (0,255,0
    """

    def __init__(self, ImageName = None, PEName = None):
        self.data = []
        self.PEName = PEName
        self.ImageName = ImageName

        if self.PEName:
            print "[+] PE to image mode."
            if not os.path.isfile(self.PEName):
                print "[-] File not found."
                exit(1)

            hexdata = binascii.hexlify(file(self.PEName, "rb").read())
            self.PENameLength = len(hexdata)
            self.bytestring = bin(int(hexdata, 16))[2:].zfill(self.PENameLength)

            self.PENameLength*=4    #hex to bit

        else:
            print "[+] Image to PE mode."
            self.PENameLength = 0
            self.bytestring = ""

    def isqrt(self,n):
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2

        return x if (x ** 2 > n) else x+1

    # receive string of bits and create file by the name [filename]
    def BitsToFile(self):
        if len(self.bytestring)> 1:
            v = int(self.bytestring, 2)
            b = bytearray()
            while v:
                b.append(v & 0xff)
                v >>= 8

            file(raw_input("[+] Insert file name >>> "),"wb").write(bytes(b[::-1]))
        else:
            print "[-] Error: No PE File Name specified."
            exit(1)

    def FileToImage(self):
        if self.PEName and self.ImageName:

            for bit in str(self.bytestring):
                if bit == "1":
                    self.data.append((0, 255, 0))
                else:
                    self.data.append((255, 0, 0))

            img = Image.new("RGB", (self.isqrt(self.PENameLength), self.isqrt(self.PENameLength)))
            img.putdata(self.data)
            img.save(self.ImageName)
            print "[+] File to image finished successfully!"
        else:
            print "[-] Error: Neither PE File specified Nor Image Name specified."

    def ImageToFile(self):
        if self.ImageName:
            if not os.path.isfile(self.ImageName):
                print "[-] File not found."
                exit(1)

            ImageFile.LOAD_TRUNCATED_IMAGES = True
            img = PngImagePlugin.Image.open(self.ImageName)
            width, height = img.size

            for i in xrange(height):
                for k in xrange(width):
                    ab = img.getpixel((k, i))
                    if ab[0] == 255 and ab[1] == 0:
                        self.bytestring += "0"
                    if ab[0] == 0 and ab[1] == 255:
                        self.bytestring += "1"

            self.BitsToFile()
            print "[+] Image to file finished successfully!"
        else:
            print "[-] Error: No Image Name specified."


if __name__ == '__main__':
    #engine = PEImage("Test.png","sleeptest.exe")
    #engine.FileToImage()
    engine = PEImage("Test.png")
    engine.ImageToFile()