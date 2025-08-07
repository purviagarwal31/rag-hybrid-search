# pipeline/embedder.py

import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from django.conf import settings

MODEL_NAME = 'all-MiniLM-L6-v2'  # Small and fast

# Path to save FAISS index and paper metadata
FAISS_INDEX_PATH = os.path.join(settings.BASE_DIR, 'embeddings', 'faiss_index.bin')
METADATA_PATH = os.path.join(settings.BASE_DIR, 'embeddings', 'metadata.pkl')

# Load embedding model
model = SentenceTransformer(MODEL_NAME)

def generate_embeddings(df, text_column='abstract'):
    """
    Generate embeddings for the text column of a DataFrame.
    """
    texts = df[text_column].tolist()
    print(f"🔍 Generating embeddings for {len(texts)} documents...")

    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    return embeddings

def build_faiss_index(embeddings):
    """
    Builds a FAISS index from numpy embeddings.
    """
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    print(f"✅ FAISS index built with {index.ntotal} vectors")
    return index

def save_index(index, df):
    """
    Saves the FAISS index and metadata.
    """
    os.makedirs(os.path.dirname(FAISS_INDEX_PATH), exist_ok=True)

    faiss.write_index(index, FAISS_INDEX_PATH)
    with open(METADATA_PATH, 'wb') as f:
        pickle.dump(df[['title', 'abstract']].to_dict(orient='records'), f)

    print(f"✅ Saved FAISS index to {FAISS_INDEX_PATH}")
    print(f"✅ Saved metadata to {METADATA_PATH}")
