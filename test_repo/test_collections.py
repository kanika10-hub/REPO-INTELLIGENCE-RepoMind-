import chromadb

client = chromadb.PersistentClient(
    path="chroma_db"
)

collections = client.list_collections()

print("\n=== COLLECTIONS ===\n")

for collection in collections:
    print(collection.name)