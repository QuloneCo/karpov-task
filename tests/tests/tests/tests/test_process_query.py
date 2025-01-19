from steps.4_process_query import process_query
import pickle

def test_process_query(tmp_path):
    texts = ["Hello world!", "Python is great!"]
    embeddings = [[0.1, 0.2], [0.3, 0.4]]

    index_file = tmp_path / "index.pkl"
    with open(index_file, 'wb') as f:
        pickle.dump((texts, embeddings), f)
    
    query = "Python"
    results = process_query(query, index_file, top_k=1)
    assert results[0] == "Python is great!"
