# rag/retrieval.py
import chromadb
from chromadb.utils import embedding_functions

from config import CHROMA_DB_PATH

client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

embedding_function = (
    embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
)

collection = client.get_collection(
    name="stem_knowledge",
    embedding_function=embedding_function
)


def retrieve_context(query, k=3):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    return "\n\n".join(results["documents"][0])