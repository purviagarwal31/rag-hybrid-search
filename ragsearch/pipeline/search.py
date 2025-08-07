# pipeline/search.py

import os
import pickle
import numpy as np
import faiss
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
from django.conf import settings
#import nltk
import re


#nltk.download('punkt')

# Load files
FAISS_INDEX_PATH = os.path.join(settings.BASE_DIR, 'embeddings', 'faiss_index.bin')
METADATA_PATH = os.path.join(settings.BASE_DIR, 'embeddings', 'metadata.pkl')

# Load metadata
with open(METADATA_PATH, 'rb') as f:
    documents = pickle.load(f)  # List of dicts with 'title' and 'abstract'

# Prepare text for BM25
corpus = [doc['abstract'] for doc in documents]
tokenized_corpus = [re.findall(r'\b\w+\b', doc.lower()) for doc in corpus]
bm25 = BM25Okapi(tokenized_corpus)

# Load FAISS index
faiss_index = faiss.read_index(FAISS_INDEX_PATH)

# Load the same embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')


def hybrid_search(query, top_k=5, alpha=0.5):
    """
    Combines FAISS and BM25 search results.
    alpha: weight between 0 (only BM25) and 1 (only FAISS)
    """

    # --- Semantic Search via FAISS ---
    query_embedding = model.encode([query])
    D, I = faiss_index.search(np.array(query_embedding), top_k)

    faiss_results = []
    for idx, score in zip(I[0], D[0]):
        faiss_results.append({
            'title': documents[idx]['title'],
            'abstract': documents[idx]['abstract'],
            'faiss_score': float(score)
        })

    # --- Keyword Search via BM25 ---
    tokenized_query = re.findall(r'\b\w+\b', query.lower())
    bm25_scores = bm25.get_scores(tokenized_query)

    # Combine results (normalize and sort)
    combined = []
    for i in range(len(documents)):
        bm25_score = bm25_scores[i]
        faiss_score = 1 / (1 + faiss_index.d + 1e-10)  # Normalize FAISS distance to relevance

        # Hybrid score (you can tweak the formula)
        score = alpha * faiss_score + (1 - alpha) * bm25_score
        combined.append((i, score))

    # Sort by score
    top_combined = sorted(combined, key=lambda x: x[1], reverse=True)[:top_k]

    # Prepare result set
    results = []
    for idx, score in top_combined:
        results.append({
            'title': documents[idx]['title'],
            'abstract': documents[idx]['abstract'],
            'score': float(score)
        })

    return results
