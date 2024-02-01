
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
import chromadb 
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

image_dir = '../Desktop/photos2019'

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


image_arrays = image_to_array(image_dir)



embedding_function = OpenCLIPEmbeddingFunction()
data_loader = ImageLoader()
client = chromadb.PersistentClient(path="/users/alf/Downloads/chroma")


collection = client.create_collection(
         name = "josei1",
         embedding_function=embedding_function,
            data_loader=data_loader
            )



image_arrays = image_to_array(image_dir)
num_images = len(image_arrays)
ids = []
for i in range(num_images):
    ids.append(f'id{i}')

if image_arrays:
    collection.add(
        ids=ids,
        images = image_arrays
    )
else:
    print("no images found")

retrieved = collection.query(
    query_texts = ["sky"]
)
for img in retrieved:
    
    plt.imshow(img)
    plt.axis("off")
    plt.show()

print(retrieved)

