# EECS 50 Extra Credit Project
# Image Filtering

import imageio
import numpy

import convolution_filters as conv

def main():
    img = imageio.imread("noisy.png")
    height, width, channels = img.shape
    img_output = img.copy()
    # use img[y,x] to get pixels
    print("Height:",height);
    print("Width:",width);
    print("Color Channels:",channels);
    print("Pixel type:",img.dtype);
    conv.blur(img_output)
    imageio.imwrite("output.png",img_output)

main()