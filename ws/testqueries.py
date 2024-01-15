import chromadb 
from matplotlib import pyplot as plt

client = chromadb.HttpClient(
        host="18.234.181.227",
        port=8000,
        headers={"X-Chroma-Token": "sk-mytoken"}
                           ) 

print(client)

collections = client.list_collections()
collection = client.get_or_create_collection(name="your_collection_nam1e1")

results = collection.query(
    query_texts=["sunset"],
    n_results=1
)


'''
retrieved = collection.query(query_texts=["sunset"], include=['data'], n_results=1)
for img in retrieved['data'][0]:
    plt.imshow(img)
    plt.axis("off")
    plt.show()


print(results)
'''
