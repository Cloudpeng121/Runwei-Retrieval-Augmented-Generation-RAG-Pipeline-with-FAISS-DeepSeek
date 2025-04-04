import pyodbc
import pandas as pd

# Define connection string
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=runwei-sql.database.windows.net,1433;"
    "DATABASE=RunweiOpportunities;"
    "UID=sql-admin;"
    "PWD=Runwei2025;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

# Connect to SQL Server
conn = pyodbc.connect(conn_str)

# Retrieve key text fields for embedding
query = """
SELECT ID, Title, Description, Eligibility, Tags, Industry, AreaOfFocus
FROM dbo.Opportunities
"""
df = pd.read_sql(query, conn)

print(df.head())  # Check data

conn.close()

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model
model = SentenceTransformer("BAAI/bge-base-en")

# Prepare text for embedding
df["combined_text"] = (
    df["Title"].fillna("") + " " +
    df["Description"].fillna("") + " " +
    df["Eligibility"].fillna("") + " " +
    df["Industry"].fillna("") + " " +
    df["AreaOfFocus"].fillna("")
)

# Generate embeddings
embeddings = model.encode(df["combined_text"].tolist(), convert_to_numpy=True)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "faiss_index_opportunities.bin")

print("✅ Embeddings generated and FAISS index saved.")
