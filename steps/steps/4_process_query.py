import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def process_query(query, index_file, top_k=3):
    with open(index_file, 'rb') as f:
        texts, embeddings = pickle.load(f)

    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([query])

    similarities = cosine_similarity(query_embedding, embeddings).flatten()
    top_indices = similarities.argsort()[-top_k:][::-1]

    results = [texts[i] for i in top_indices]
    return results
