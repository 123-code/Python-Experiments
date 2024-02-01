import matplotlib.pyplot as plt
import chromadb
client = chromadb.PersistentClient(path="/users/alf/Downloads/chroma")
collection = client.get_or_create_collection(name="photosembedjding123o4i6")

print(collection)

retrieved = collection.query(query_texts=["sunset"], include=['data'], n_results=1)
