import chromadb
from chromadb.utils.embedding_functions import (
    SentenceTransformerEmbeddingFunction,
)

from app.config import CHROMA_PATH, COLLECTION

_embedding = SentenceTransformerEmbeddingFunction(
    model_name="BAAI/bge-m3",
)

_client = chromadb.PersistentClient(CHROMA_PATH)


def get_collection():
    return _client.get_or_create_collection(
        name=COLLECTION,
        embedding_function=_embedding,
    )