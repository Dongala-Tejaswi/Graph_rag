import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer
from backend.graph.neo4j_graph import get_graph_context

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

index = faiss.read_index(
    "embeddings/faiss_index.bin"
)

with open(
    "embeddings/documents.pkl",
    "rb"
) as f:
    documents = pickle.load(f)

def retrieve_context(query):

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding),
        k=3
    )

    vector_results = []

    for idx in I[0]:
        vector_results.append(documents[idx])

    graph_results = get_graph_context(query)

    final_context = "\n".join(
        vector_results + graph_results
    )

    return final_context