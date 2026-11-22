
import numpy

def fourier_transform(img, filter_matrix):
    height, width, channels = img.shape
    output = numpy.zeros_like(img)
    for c in range(channels):
        fft = numpy.fft.fft2(img[:, :, c])
        fft_shifted = numpy.fft.fftshift(fft)
        filtered = fft_shifted * filter_matrix
        inverse_shift = numpy.fft.ifftshift(filtered)
        inverse_fft = numpy.fft.ifft2(inverse_shift)
        output[:, :, c] = numpy.clip(
            numpy.real(inverse_fft), 0, 255
        ).astype(numpy.uint8)
    return output


"""
Reduces image noise by removing high-frequency components
using the Fourier Transform.
"""
def low_pass(img, cutoff=15):
    height, width, channels = img.shape
    y, x = numpy.ogrid[:height, :width]
    center_y = height // 2
    center_x = width // 2
    distance = numpy.sqrt(
        (x - center_x)**2 + (y - center_y)**2
    )
    filter_matrix = (distance <= cutoff).astype(float)
    return fourier_transform(img, filter_matrix)

"""
Emphasizes image edges, fine details, and high-frequency noise
by removing low-frequency components using the Fourier Transform.
"""
def high_pass(img, cutoff=10):
    height, width, channels = img.shape
    y, x = numpy.ogrid[:height, :width]
    center_y = height // 2
    center_x = width // 2
    distance = numpy.sqrt(
        (x - center_x)**2 + (y - center_y)**2
    )
    filter_matrix = (distance > cutoff).astype(float)
    return fourier_transform(img, filter_matrix)
