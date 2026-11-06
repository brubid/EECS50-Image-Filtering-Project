import imageio
import numpy
def convolution(img, conv_matrix,row_col_size,img_y,img_x):
    height, width, channels = img.shape
    result = 0
    offset = int(row_col_size/2)
    if(row_col_size%2 == 1):
        offset = int((row_col_size-1)/2)
    for y in range(row_col_size):
        for x in range(row_col_size):
            result += conv_matrix[y,x]*img[int(img_y-offset+y)%height,int(img_x-offset+x)%width]
    return result


def blur(img):
    height, width, channels = img.shape
    blur_matrix = numpy.array([[1/9.0,1/9.0,1/9.0],
                              [1/9.0,1/9.0,1/9.0],
                              [1/9.0,1/9.0,1/9.0]])
    for y in range(height):
        for x in range(width):
            img[y,x]=convolution(img,blur_matrix,3,y,x)
    return img