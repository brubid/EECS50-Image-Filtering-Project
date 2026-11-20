import imageio
import numpy

def scale_img(img,y_scale,x_scale):
    height, width, channels = img.shape
    img_scaled = numpy.zeros((int(height*y_scale),int(width*x_scale),channels),dtype=img.dtype)
    for y in range(int(height*y_scale)):
        for x in range(int(width*x_scale)):
            img_scaled[y,x] = img[int(y/y_scale),int(x/x_scale)]

    return img_scaled