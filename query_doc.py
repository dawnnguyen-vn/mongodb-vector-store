from create_vector_store import vector_store

results = vector_store.similarity_search(
    "Your query", k=2
)

# Return Document
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")
    print("-------------------------")