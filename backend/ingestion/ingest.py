import os
import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

documents = []

with open("data/sample.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    documents.append(line.strip())

embeddings = model.encode(documents)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

faiss.write_index(
    index,
    "embeddings/faiss_index.bin"
)

with open("embeddings/documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print("Embeddings stored successfully")