import chromadb 
from matplotlib import pyplot as plt

client = chromadb.HttpClient(
        host="18.234.181.227",
        port=8000,
        headers={"X-Chroma-Token": "sk-mytoken"}
                           ) 

print(client)

collections = client.list_collections()
<<<<<<< HEAD
collection = client.get_or_create_collection(name="your_collection_nam1e1")


retrieved = collection.query(query_texts=["sunset"], include=['data'], n_results=1)
for img in retrieved['data'][0]:
=======
collection = client.get_or_create_collection(name="my_photosfeftr")
print(collection)
results = collection.query(
    query_texts=["sunset"],
    n_results=1
)



retrieved = collection.query(query_texts=["party"], include=['data'], n_results=1)
for img in retrieved['data'][1]:
>>>>>>> dbffad4a37689c02dbd9afb58458c2560c4aee06
    plt.imshow(img)
    plt.axis("off")
    plt.show()


<<<<<<< HEAD
print(retrieved)
=======
print(results)
>>>>>>> dbffad4a37689c02dbd9afb58458c2560c4aee06

