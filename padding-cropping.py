import numpy as np
from PIL import Image

def prepare_image(
image: np.ndarray, # (1, H, W)
width: int,
height: int,
x: int,
y: int,
size: int
) -> tuple[np.ndarray, np.ndarray]:
    
    if len(image.shape) != 3: # image isn't 3D
        raise ValueError
    else:
        if image.shape[0] != 1: # number of channels isn't 1
            raise ValueError
        else:
            if width < 32 or height < 32 or size < 32:
                raise ValueError
            if x < 0 or x + size > width:
                raise ValueError
            if y < 0 or y +size > height:
                raise ValueError
            
            original_height = image.shape[1]
            original_width = image.shape[2]
            n = 0 # counter for cropping
            m = 0 # counter for cropping
            a = 0 # counter for padding
            b = 0 # counter for padding
            
            # the cropping and padding parts:

            if original_height > height: # cropping
                n += 1
                crop_height = (original_height - height) // 2
                copy_image = image[:, crop_height:crop_height+height, :]
            elif original_height < height: # padding
                a += 1
                pad_height = (height - original_height) // 2
                bottom = height - original_height - pad_height
                copy_image = np.pad(image, ((0, 0),
                                            (pad_height, bottom), (0, 0)), mode='edge')

            if original_width > width: # cropping
                m += 1
                crop_width = (original_width - width) // 2
                if n == 1: # the image also had cropping on its height
                    copy_image = copy_image[:, :, crop_width:crop_width+width]
                elif a == 1: # the image already had padding on height
                    copy_image = copy_image[:, :, crop_width:crop_width+width]
                else: # cropping is done only on width and without any padding on height
                    copy_image = image[:, :, crop_width:crop_width+width]
            elif original_width < width: # padding
                b += 1
                pad_width = (width - original_width) // 2
                right = width - original_width - pad_width
                if a == 0 and n == 0: # image had neither padding nor cropping on height
                    copy_image = np.pad(image, ((0, 0), (0, 0), (pad_width, right)), mode='edge')
                if a == 1 or n == 1: # image already had padding or cropping on height
                    copy_image = np.pad(copy_image, ((0, 0), (0, 0), (pad_width, right)),
                                        mode='edge')
                
            
            if n == 1 or m == 1 or a == 1 or b == 1: # cropping/padding was applied for at least
                # 1 dimension
                sub_area = copy_image[:, y:y+size, x:x+size]
                return (copy_image, sub_area)
            if n == 0 and m == 0 and a == 0 and b == 0: # no cropping/padding was applied
                sub_area = image[:, y:y+size, x:x+size]
                return (image, sub_area)
    
        
#---------
if __name__ == "__main__":
    with Image.open("grayscale_image.jpg") as im:
        arr = np.array(im)
        arr = arr.reshape(1, *arr.shape)
        res = prepare_image(arr, 5000, 2000, 1000, 1000, 500)
        print(res[0].shape)
        print("\n",res[1].shape)
        

        
        
