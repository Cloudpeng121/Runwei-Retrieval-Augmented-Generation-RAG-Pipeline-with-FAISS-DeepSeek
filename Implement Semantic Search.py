import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# Load your original data used to build FAISS
df = pd.read_csv("opportunities_metadata.csv")  # Make sure this file was saved earlier!

# Load FAISS index and model
index = faiss.read_index("faiss_index_opportunities.bin")
model = SentenceTransformer("BAAI/bge-base-en")

# Sample user query
query = "Funding opportunities for Black entrepreneurs in California"
query_embedding = model.encode([query], convert_to_numpy=True)

# Search top 5 matches
top_k = 5
D, I = index.search(query_embedding, top_k)

# Display results
for idx in I[0]:
    print("🔹 Title:", df.iloc[idx]["Title"])
    print("📌 Description:", df.iloc[idx]["Description"][:300])  # Preview
    print("🌐 URL:", df.iloc[idx].get("Url", "N/A"))
    print("---")
