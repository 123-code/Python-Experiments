
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
import chromadb 
from PIL import Image
import numpy as np
import io 


def image_to_array(image_path):
    image = Image.open(image_path)

    numpy_array = np.asarray(image)
  
    return numpy_array



image1 = image_to_array('../Downloads/IMG_4477.jpeg')

embedding_function = OpenCLIPEmbeddingFunction()
data_loader = ImageLoader()
client = chromadb.PersistentClient(path="/users/joseignacionaranjo/Downloads/chroma")

collection = client.create_collection(
    name = "photoscollection1",
    embedding_function=embedding_function,
    data_loader=data_loader
)


collection.add(
    ids=['id1'],
    images = [image1]
)

result = collection.query(
    query_texts = ["sky"]
)

print(result)

