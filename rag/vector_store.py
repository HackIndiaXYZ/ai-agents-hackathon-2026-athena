# rag/vector_store.py
import sys
import os

project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(project_root)

import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
from config import DATASET_PATH, CHROMA_DB_PATH


def build_vector_store():
    # Load dataset
    df = pd.read_csv(DATASET_PATH)

    # Initialize ChromaDB client
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

    # Gemini doesn't currently provide direct embeddings through Chroma,
    # so we'll use a SentenceTransformer embedding model.
    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    # Delete old collection if it exists
    try:
        client.delete_collection("stem_knowledge")
    except:
        pass

    collection = client.create_collection(
        name="stem_knowledge",
        embedding_function=embedding_function
    )

    documents = []
    metadatas = []
    ids = []

    for idx, row in df.iterrows():

        content = f"""
        Subject: {row['subject']}
        Topic: {row['topic']}
        Difficulty: {row['difficulty']}

        Question:
        {row['question']}

        Answer:
        {row['answer']}

        Explanation:
        {row['enhanced_completion']}
        """

        documents.append(content)

        metadatas.append({
            "subject": str(row["subject"]),
            "topic": str(row["topic"]),
            "difficulty": str(row["difficulty"])
        })

        ids.append(str(idx))

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print(f"Added {len(documents)} documents to ChromaDB")


if __name__ == "__main__":
    build_vector_store()