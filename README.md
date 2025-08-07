# 🔍 RAG Hybrid Search

A lightweight and effective **Retrieval-Augmented Generation (RAG)** system combining **FAISS Embeddings** and **BM25** for hybrid search over AI research papers.

---

## 🚀 Features

- ✅ FAISS vector search using `sentence-transformers`
- ✅ BM25 traditional keyword-based search using `rank_bm25`
- ✅ Hybrid scoring combining dense + sparse retrieval
- ✅ Django-powered backend with REST API
- ✅ Streamlit frontend for quick search demo

---

## 📁 Project Structure

rag-hybrid-search/
│
├── backend/
│ ├── manage.py
│ ├── ragsearch/ # Django project
│ └── pipeline/ # Django app
│ ├── views.py # View logic (index, search, API)
│ ├── search.py # Core hybrid search logic
│ ├── bm25.py # BM25 setup
│ ├── vector_store.py # FAISS setup
│ └── data/ # Your .pkl and .jsonl files
│
├── frontend/
│ └── frontend.py # Streamlit app
│
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/purviagarwal31/rag-hybrid-search.git
cd rag-hybrid-search

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt
🧠 Running the Backend (Django)
bash
Copy
Edit
# Navigate into backend folder
cd backend

# Run the Django server
python manage.py runserver
Access at: http://127.0.0.1:8000/

📡 Search API
sql
Copy
Edit
GET /api/search/?q=your_query
Example:

ruby
Copy
Edit
GET http://127.0.0.1:8000/api/search/?q=AI
💻 Streamlit Frontend
bash
Copy
Edit
streamlit run frontend/frontend.py
It provides a simple UI to test hybrid search results.

📊 Technologies Used
Python 3.10+

Django for backend

FAISS for dense vector search

BM25 using rank_bm25

sentence-transformers

Streamlit for frontend demo

REST Framework (optional)

📂 Sample Query Results
Query: "Recent advances in reinforcement learning"

A Short Survey On Memory Based Reinforcement Learning

Grounding Artificial Intelligence in the Origins of Human Behavior

A Survey of Reinforcement Learning Techniques

...

🤝 Acknowledgements
This project was submitted as part of a RAG System Interview Assignment.
Thanks to the reviewing team for the opportunity!

📌 Author
Purvi Agarwal
GitHub
LinkedIn


