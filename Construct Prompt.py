import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# Load FAISS index and embedding model
index = faiss.read_index("faiss_index_opportunities.bin")
model = SentenceTransformer("BAAI/bge-base-en")

# Load metadata
df = pd.read_csv("opportunities_metadata.csv")  # Must match the data used during embedding

# User query
user_query = "Is there a grant available for women founders in tech?"
query_embedding = model.encode([user_query], convert_to_numpy=True)

# FAISS search (Top-k)
top_k = 5
D, I = index.search(query_embedding, top_k)  # Now I is defined

# Build prompt using retrieved results
retrieved_context = "\n\n".join([
    f"Title: {df.iloc[idx]['Title']}\nDescription: {df.iloc[idx]['Description']}"
    for idx in I[0]
])


prompt = f"""You are a grant advisor. Based on the following retrieved opportunities, answer the user's question:

Context:
{retrieved_context}

Question: {user_query}

Answer:"""

# Show prompt
print(prompt)
