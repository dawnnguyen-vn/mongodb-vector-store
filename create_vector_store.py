from langchain_huggingface import HuggingFaceEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient

# Embedding model convert text to vector
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# Connect to MongoDB Cluster
client = MongoClient("mongodb://localhost:27017/?directConnection=true")

# Database info
DB_NAME = "vector_database"
COLLECTION_NAME = "vector_collection"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "index-vectorstores"

MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

# Create vector store
vector_store = MongoDBAtlasVectorSearch(
    collection=MONGODB_COLLECTION,
    embedding=embeddings,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
)

# Create vector search index on the collection
# Since we are using the default OpenAI embedding model (ada-v2) we need to specify the dimensions as 1536
vector_store.create_vector_search_index(dimensions=768)





