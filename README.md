readme_content = """
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

```bash
runwei/
├── Embeddings.py                 # Load data and generate FAISS index
├── opportunities_metadata.csv   # Metadata file saved from Azure SQL
├── faiss_index_opportunities.bin # FAISS index
├── Implement Semantic Search.py # Search & retrieve relevant docs
├── Construct Prompt.py          # Build context + prompt
├── DeepSeekChat.py              # Send prompt to DeepSeek
└── README.md                    # This file
