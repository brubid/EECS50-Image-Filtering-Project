import imageio
import numpy
def convolution(img, conv_matrix,row_col_size,img_y,img_x, apply_on_alpha):
    height, width, channels = img.shape
    result_add = 0
    result_sub = 0
    offset = int(row_col_size/2)
    if(row_col_size%2 == 1):
        offset = int((row_col_size-1)/2)
    for y in range(row_col_size):
        for x in range(row_col_size):
            if(conv_matrix[y,x] > 0):
                result_add += conv_matrix[y,x]*img[int(img_y-offset+y)%height,int(img_x-offset+x)%width]
            else:
                result_sub += abs(conv_matrix[y,x])*img[int(img_y-offset+y)%height,int(img_x-offset+x)%width]
    if not apply_on_alpha and channels is 4:
        alpha = img[img_y,img_x][3]
        pixel = numpy.where(result_add>result_sub,result_add-result_sub,0)
        pixel[3]=alpha
        return pixel
    return  numpy.where(result_add>result_sub,result_add-result_sub,0)
   
    

def image_filter(img,conv_matrix,row_col_size,apply_on_alpha):
    height, width, channels = img.shape
    for y in range(height):
        for x in range(width):
            img[y,x]=convolution(img,conv_matrix,row_col_size,y,x,apply_on_alpha)
    return img
def box_blur(img,intensity):
    row_col_size = 2*max(intensity,0)+1
    blur_matrix = numpy.ones((row_col_size,row_col_size))/(row_col_size*row_col_size)
    return image_filter(img,blur_matrix,row_col_size)


def sharpen(img):
    sharpen_matrix = numpy.array([[0,-1,0],
                              [-1,5,-1],
                              [0,-1,0]])
    return image_filter(img,sharpen_matrix,3,False)