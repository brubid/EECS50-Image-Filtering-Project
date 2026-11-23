import imageio
import numpy
def convolution(img, conv_matrix,row_col_size,img_y,img_x, apply_on_alpha):
    height, width, channels = img.shape
    result = numpy.zeros(channels, dtype=numpy.float64)

    offset = int(row_col_size/2)

    for y in range(row_col_size):
        for x in range(row_col_size):
            result += (conv_matrix[y,x]*(img[int(img_y-offset+y)%height,int(img_x-offset+x)%width])).astype(numpy.float64)
            
    if(channels==4) and not apply_on_alpha:
        result[3] = img[img_y,img_x][3]
    result = numpy.clip(result,0,255).astype(numpy.uint8)
    return result
  
   
    

def image_filter(img,conv_matrix,row_col_size,apply_on_alpha):
    height, width, channels = img.shape
    img_copy=img.copy()
    for y in range(int(height)):
        for x in range(int(width)):
            img[y,x]=convolution(img_copy,conv_matrix,row_col_size,y,x,apply_on_alpha)
    return img
def box_blur(img,intensity):
    row_col_size = 2*max(intensity,0)+1
    blur_matrix = numpy.ones((row_col_size,row_col_size))/(row_col_size*row_col_size)
    return image_filter(img,blur_matrix,row_col_size,True)


def sharpen(img):
    sharpen_matrix = numpy.array([[0,-1,0],
                              [-1, 5,-1],
                              [0,-1,0]])
    return image_filter(img,sharpen_matrix,3,False)

def edge_detect(img):
    sharpen_matrix = numpy.array([[0,-1,0],
                              [-1,4,-1],
                              [0,-1,0]])
    return image_filter(img,sharpen_matrix,3,False)