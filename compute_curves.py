import numpy as np
import os, sys
from PIL import Image
import matplotlib.pyplot as plt

SIZE = 1080

filters = [
    'Clarendon', 'Gingham', 'Moon', 'Lark', 'Reyes', 'Juno', 'Slumber',
    'Crema', 'Ludwig', 'Aden', 'Perpetua', 'Amaro', 'Mayfair', 'Rise',
    'Hudson', 'Valencia', 'X-Pro-II', 'Sierra', 'Willow', 'Lo-Fi', 'Inkwell',
    'Hefe', 'Nashville', 'Stinson', 'Vesper', 'Earlybird', 'Brannan', 'Sutro',
    'Toaster', 'Walden', '1977', 'Kelvin', 'Maven', 'Ginza', 'Skyline',
    'Dogpatch', 'Brooklyn', 'Helena', 'Ashby', 'Charmes'
]

for n in range(len(filters)):
    in_file = 'input/%d.jpg' % (n + 1)
    with Image.open(in_file) as im:
        img = np.array(im)

    # look at a circle with diameter of SIZE * 0.3
    r_curve = np.zeros((255), int)
    g_curve = np.zeros((255), int)
    b_curve = np.zeros((255), int)
    for deg in range(255):
        th = deg / 255.0 * 2.0 * np.pi
        x = -np.cos(th) * SIZE * 0.3
        y = np.sin(th) * SIZE * 0.3

        r = img[int(y + SIZE / 2), int(x + SIZE / 2), 0]
        g = img[int(y + SIZE / 2), int(x + SIZE / 2), 1]
        b = img[int(y + SIZE / 2), int(x + SIZE / 2), 2]

        r_curve[deg] = r
        g_curve[deg] = g
        b_curve[deg] = b

    fig = plt.figure()
    ax = fig.gca()
    ax.plot(r_curve, color='r')
    ax.plot(g_curve, color='g')
    ax.plot(b_curve, color='b')
    ax.set_title(filters[n])
    ax.set_xlim((0, 255))
    ax.set_ylim((0, 255))
    ax.set_xticks([0, 63.75, 127.5, 191.25, 255])
    ax.set_yticks([0, 63.75, 127.5, 191.25, 255])
    ax.set_aspect('equal')
    ax.grid()
    # plt.show()

    plt.savefig('output/%s.png' % filters[n])
    plt.close(fig)
