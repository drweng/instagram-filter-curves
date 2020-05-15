# theta [0-360] --> [0, 255]

import numpy as np
import os, sys
from PIL import Image

SIZE = 1080

img = np.zeros((SIZE, SIZE, 3), float)
for i in range(SIZE):
    for j in range(SIZE):
        x = i - SIZE / 2
        y = j - SIZE / 2
        if y == 0:
            if x > 0:
                th = np.pi
            else:
                th = 0
        elif y > 0:
            th = np.arctan(x / y) + np.pi / 2.0
        else:
            th = np.arctan(x / y) + np.pi * 3.0 / 2.0

        img[j, i, 0] = th / 2.0 / np.pi * 255.0
        img[j, i, 1] = th / 2.0 / np.pi * 255.0
        img[j, i, 2] = th / 2.0 / np.pi * 255.0

a = img.astype(np.uint8)
print(a.max())
print(a.min())
im = Image.fromarray(img.astype(np.uint8))
# im.show()
outfile = "test_pic.png"
im.save(outfile)
