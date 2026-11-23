# EECS 50 Extra Credit Project
# Image Filtering

import tkinter.filedialog
import PIL.ImageTk
import imageio
import numpy
from scale import scale_img
import convolution_filters as conv
import tkinter
from tkinter import ttk
import fourier_filters as fourier

import PIL
def main():
    root = tkinter.Tk()
    root.title("EECS 50 - Image Processing")
    width = int(root.winfo_screenwidth())
    height = int(root.winfo_screenheight())
    root.geometry(f"{width}x{height}")
    root.resizable(False, False)
    window_frame = ttk.Frame(root)
    window_frame.pack(fill=tkinter.BOTH, expand=True)
    exit_button = ttk.Button(window_frame, text="Exit",command=root.destroy)
    exit_button.pack(pady=10)

    # display original image
    img_path = tkinter.filedialog.askopenfilename(title="Select image",initialdir=".")

    img = imageio.imread(img_path)
    height, width, channels = img.shape
    img_output = img.copy()
    # use img[y,x] to get pixels
    print("Image Info")
    print("Height:",height);
    print("Width:",width);
    print("Color Channels:",channels);
    print("Pixel type:",img.dtype);
    img_PIL = PIL.Image.fromarray(img)
    # should resize
    img_tk = PIL.ImageTk.PhotoImage(img_PIL)
    img_label = tkinter.Label(root, image=img_tk,compound=tkinter.BOTTOM,text="Original")
    img_label.pack(pady=20)



    # show image output
    img_output = img.copy()
  #  img_output = fourier.high_pass(img_output)
   # conv.sharpen(img_output)
    conv.sharpen(img_output)
    out_img_PIL = PIL.Image.fromarray(img_output)
    out_img_tk = PIL.ImageTk.PhotoImage(out_img_PIL)
    out_img_label = tkinter.Label(root, image=out_img_tk,compound=tkinter.BOTTOM,text="Sharpen")
    out_img_label.pack(pady=100)


    root.mainloop()
    
    '''
    img = imageio.imread("input2.png")
    height, width, channels = img.shape
    img_output = img.copy()
    # use img[y,x] to get pixels
    print("Image Info")
    print("Height:",height);
    print("Width:",width);
    print("Color Channels:",channels);
    print("Pixel type:",img.dtype);
    conv.sharpen(img_output)
   # conv.box_blur(img_output,2)

    img_output = scale_img(img_output,1,2.5)
    imageio.imwrite("output.png",img_output)
    '''
main()