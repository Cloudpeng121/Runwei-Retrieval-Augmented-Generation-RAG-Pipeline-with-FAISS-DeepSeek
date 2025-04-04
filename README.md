# Runwei: Retrieval-Augmented Generation (RAG) Pipeline with FAISS & DeepSeek

This project demonstrates how to build a Retrieval-Augmented Generation (RAG) system using FAISS for semantic search and DeepSeek AI for large language model responses, applied to a real-world dataset of funding opportunities.

---

## 🔧 Tools & Stack

- **Python 3.10** (conda environment)
- **FAISS** (Facebook AI Similarity Search)
- **Sentence-Transformers** (Embedding via `BAAI/bge-base-en`)
- **DeepSeek LLM API** (chat completion endpoint)
- **Azure SQL** (data source)
- **Pandas, NumPy, PyODBC** (ETL & data handling)

---

## 📁 Project Structure

```
runwei/
├── Embeddings.py                   # Load data and generate FAISS index
├── opportunities_metadata.csv     # Metadata file saved from Azure SQL
├── faiss_index_opportunities.bin  # FAISS index
├── Implement Semantic Search.py   # Search & retrieve relevant docs
├── Construct Prompt.py            # Build context + prompt
├── DeepSeekChat.py                # Send prompt to DeepSeek
└── README.md                      # This file
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Cloudpeng121/Runwei-Retrieval-Augmented-Generation-RAG-Pipeline-with-FAISS-DeepSeek.git
cd Runwei-Retrieval-Augmented-Generation-RAG-Pipeline-with-FAISS-DeepSeek
```

### 2. Create environment

```bash
conda create -n runwei-env python=3.10
conda activate runwei-env
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗃️ Export SQL Data

Use `pyodbc` to extract data from Azure SQL and save it as `opportunities_metadata.csv`:

```python
# inside Embeddings.py
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
df.to_csv("opportunities_metadata.csv", index=False)
```

---

## 🧠 Generate Embeddings

```bash
python Embeddings.py
```

This will:
- Load metadata from SQL
- Generate sentence embeddings using `BAAI/bge-base-en`
- Store vector index in `faiss_index_opportunities.bin`

---

## 🔍 Run Semantic Search

```bash
python Implement Semantic Search.py
```

This script:
- Loads FAISS index
- Accepts a user query
- Returns the top 5 semantically matched documents

---

## ✨ Construct Prompt

```bash
python Construct Prompt.py
```

This script:
- Combines top-k semantic results
- Formats a user query with context
- Outputs a natural-language prompt for the LLM

---

## 🤖 DeepSeek RAG Response

### Set your DeepSeek API key (PowerShell)

```bash
$env:DEEPSEEK_API_KEY = "your-api-key"
```

### Run the chat interface

```bash
python DeepSeekChat.py
```

### Or use code:

```python
import requests, os

headers = {
    "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
    "Content-Type": "application/json"
}

payload = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "You are a helpful grant advisor."},
        {"role": "user", "content": prompt}
    ]
}

response = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=payload)
print(response.json()["choices"][0]["message"]["content"])
```

---

## ✅ Sample Result

**Query:** _"Is there a grant available for women founders in tech?"_

**DeepSeek Answer:**

Yes, based on the retrieved opportunities, there are several grants available for women founders in tech, such as:
- StartHER Grant
- San Francisco Women's Entrepreneurship Fund
- About Her Culture Micro Grant

---

## 📄 License

MIT License.

---

## ✨ Author

Yunpeng Wang  
[LinkedIn](http://www.linkedin.com/in/yunpeng-wang-a33215247)

├── faiss_index_opportunities.bin # FAISS index
├── Implement Semantic Search.py # Search & retrieve relevant docs
├── Construct Prompt.py          # Build context + prompt
├── DeepSeekChat.py              # Send prompt to DeepSeek
└── README.md                    # This file

