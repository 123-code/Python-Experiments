import chromadb 
import requests 

url = 'http://localhost:8000/api/v1/collections'
headers = {
    'X-CHROMA-TOKEN': ADDTOKEN
}
data = {'key': 'value'}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)
