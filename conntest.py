
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
import chromadb 
from PIL import Image
import numpy as np
import os

image_dir = './uploads'

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



#image1 = image_to_array('../Downloads/IMG_4477.jpeg')

embedding_function = OpenCLIPEmbeddingFunction()
data_loader = ImageLoader()
client = chromadb.PersistentClient(path="/users/joseignacionaranjo/Downloads/chroma")




collection = client.create_collection(
         name = "photosembedding1234",
         embedding_function=embedding_function,
            data_loader=data_loader
            )



image_arrays = image_to_array(image_dir)

if image_arrays:
    collection.add(
        ids=['id1'],
        images = image_arrays
    )
else:
    print("no images found")

result = collection.query(
    query_texts = ["sky"]
)

print(result)

