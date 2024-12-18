from uuid import uuid4
from create_vector_store import vector_store
from langchain_core.documents import Document

document_1 = Document(
    page_content="Your content",
    metadata={"source": ""},
)

document_2 = Document(
    page_content="Your content",
    metadata={"source": ""},
)

documents = [
    document_1,
    document_2,
]

# create a list of id for documents
uuids = [str(uuid4()) for _ in range(len(documents))]

# add documents to vector store
vector_store.add_documents(documents=documents, ids=uuids)