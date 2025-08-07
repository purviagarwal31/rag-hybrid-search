import streamlit as st
import requests

st.set_page_config(page_title="RAG Hybrid Search", page_icon="🔍")

st.title("🔍 RAG Hybrid Search")
st.subheader("Enter your query to search AI research papers")

query = st.text_input("Search Query", placeholder="e.g. Reinforcement Learning, Transformers, etc.")

if query:
    url = f"http://127.0.0.1:8000/api/search/?q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        results = response.json()
        st.success(f"Showing results for: `{query}`")

        for r in results:
            with st.expander(r["title"]):
                st.markdown(f"**Score:** `{r['score']:.2f}`")
                st.markdown(r["abstract"])
    else:
        st.error("Error fetching results from API. Make sure your Django server is running.")
