import numpy as np
from PIL import Image

def to_grayscale(pil_image: np.ndarray) -> np.ndarray:
    
    if len(pil_image.shape) == 2: # image is 2D and so already a grayscale.
        coppied_arr = np.copy(pil_image)
        coppied_arr = coppied_arr.reshape(1,*coppied_arr.shape)
        return coppied_arr
        
    elif len(pil_image.shape) == 3: # image is 3D
        if pil_image.shape[2] != 3: # the 3rd dimension's size != 3 so doesn't represent RGB=3
            raise ValueError
        else: # image is 3D and has 3 RGB channels
            normalaized_values = pil_image / 255.0
            # np.where(condition, x, y) a.k.a if condition is True, returns x, otherwise returns y
            # Also, RGB are in order (R = 0, G = 1, B = 2)
            # using the colorimetric conversion on RGB channels:
            r_linear = np.where(normalaized_values[..., 0] <= 0.04045,
                                normalaized_values[..., 0] / 12.92,
                                ((normalaized_values[..., 0] + 0.055) / 1.055) ** 2.4)
            g_linear = np.where(normalaized_values[..., 1] <= 0.04045,
                                normalaized_values[..., 1] / 12.92,
                                ((normalaized_values[..., 1] + 0.055) / 1.055) ** 2.4)
            b_linear = np.where(normalaized_values[..., 2] <= 0.04045,
                                normalaized_values[..., 2] / 12.92,
                                ((normalaized_values[..., 2] + 0.055) / 1.055) ** 2.4)
            
            # the formula:
            y_linear = 0.2126 * r_linear + 0.7152 * g_linear + 0.0722 * b_linear
        
            y = np.where(y_linear <= 0.0031308,
                        12.92 * y_linear,
                        1.055 * y_linear ** (1/2.4) - 0.055)
            
            grayscale_im = (y * 255.0).reshape((1, *y.shape)).astype(pil_image.dtype)

            if (np.issubdtype(grayscale_im.dtype, np.integer)):
                grayscale_im.round(decimals=0, out=None)
            return grayscale_im
        
    else: # image is neither 2D nor 3D
        raise ValueError
    
#---------
if __name__ == "__main__":
    input_path = "04_images/000/desert(107).jpg"
    with Image.open(input_path) as im:
        arr = np.array(im)
        print(arr.shape)
        result = to_grayscale(arr)
        print(result.shape)
