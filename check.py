import chromadb 
import requests 
'''
url = 'http://localhost:8000/api/v1/collections'
headers = {
    'X-CHROMA-TOKEN': 'new_token'
}
data = {'key': 'value'}

response = requests.get(url, headers=headers)
'''
client = chromadb.HttpClient(
  host="18.234.181.227",port=8000,
  headers={"X-Chroma-Token": "sk-mytoken"}
)

collection = client.get_collection(name="photosembedding1")
