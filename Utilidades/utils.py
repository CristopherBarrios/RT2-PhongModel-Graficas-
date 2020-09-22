# Cristopher Jose Rodolfo Barrios Solis 18207
# RT2

import struct


def char(c):
    return struct.pack("=c", c.encode("ascii"))


def word(w):
    return struct.pack("=h", w)


def dword(d):
    return struct.pack("=l", d)


class Color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, offset_color):
        r = self.r + offset_color.r
        g = self.g + offset_color.g
        b = self.b + offset_color.b

        return Color(r, g, b)

    def __mul__(self, other):
        r = self.r * other
        g = self.g * other
        b = self.b * other
        return Color(r, g, b)

    def toBytes(self):
        self.r = int(max(min(self.r, 255), 0))
        self.g = int(max(min(self.g, 255), 0))
        self.b = int(max(min(self.b, 255), 0))
        return bytes([self.b, self.g, self.r])

    __rmul__ = __mul__


def writebmp(filename, width, height, pixels):
    f = open(filename, "bw")

    f.write(char("B"))
    f.write(char("M"))
    f.write(dword(14 + 40 + width * height * 3))
    f.write(dword(0))
    f.write(dword(14 + 40))

    f.write(dword(40))
    f.write(dword(width))
    f.write(dword(height))
    f.write(word(1))
    f.write(word(24))
    f.write(dword(0))
    f.write(dword(width * height * 3))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))

    for x in range(height):
        for y in range(width):
            f.write(pixels[x][y].toBytes())
    f.close()
