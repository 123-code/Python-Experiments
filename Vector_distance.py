import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity


def generate_image_embedding(image_path, model):
    img = Image.open(image_path)
    img = img.resize((224, 224))  
    img = np.expand_dims(img, axis=0)  
    img = preprocess_input(img)  
    embedding = model.predict(img) 
    return embedding


model = VGG16(weights='imagenet', include_top=False)


image_path1 = 'path_to_image1.jpg'
image_path2 = 'path_to_image2.jpg'


embedding1 = generate_image_embedding(image_path1, model)
embedding2 = generate_image_embedding(image_path2, model)


similarity_score = cosine_similarity(embedding1, embedding2)
print("Cosine Similarity Score:", similarity_score)