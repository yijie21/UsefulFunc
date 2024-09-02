import OpenEXR
import Imath
import array
import numpy as np

def readExrToNp(filename):
    file = OpenEXR.InputFile(filename)
    dw = file.header()['dataWindow']
    size = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
    FLOAT = Imath.PixelType(Imath.PixelType.FLOAT)
    (R, G, B) = [array.array('f', file.channel(Chan, FLOAT)).tolist() for Chan in ("R", "G", "B")]
    img = np.array([R, G, B])
    img = np.transpose(img.reshape(3, size[1], size[0]), (1, 2, 0))
    return img