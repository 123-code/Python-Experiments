import os
import numpy as np
from PIL import Image

def image_to_array(image_path):
    image_paths = [os.path.join(image_path,filename) for filename in os.listdir(image_path)]
    image_arrays = []
    for x in image_paths:
        try:
            image = Image.open(x)
            numpy_array = np.asarray(image)
            image_arrays.append(numpy_array)
        except Exception as e:
            print(e)
  
    return image_arrays
