import chromadb
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
from flask import Flask, request, jsonify
import os 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/upload',methods=['POST'])

def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'no file'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'empty filename'}), 400
    
    if file:
        upload_foler = 'uploads'
        if not os.path.exists(upload_foler):
            os.makedirs(upload_foler)

        filename = os.path.join(upload_foler, file.filename)
        file.save(filename)
        return jsonify({'filename': filename}), 200
    else:
        return jsonify({'error': 'no file'}), 400


@app.route('/chromadb')
def chromadb_route():
    embedding_function = OpenCLIPEmbeddingFunction()
    image_loader = ImageLoader()
    
    client = chromadb.HttpClient(
        host="18.234.181.227",
        port=8000,
        headers={"X-Chroma-Token": "sk-mytoken"}
    )
    
    collections = client.list_collections()
    print(collections)
    
    collection = client.create_collection(
        name='multimodal_collection',
        embedding_function=embedding_function,
        data_loader=image_loader
    )
    
    return 'ChromaDB code executed'
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
