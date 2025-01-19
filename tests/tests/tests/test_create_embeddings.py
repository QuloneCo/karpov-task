from steps.3_create_embeddings import create_embeddings
import pickle

def test_create_embeddings(tmp_path):
    input_file = tmp_path / "input.txt"
    input_file.write_text("Hello world!\n---\nPython is great!")

    output_index = tmp_path / "index.pkl"
    create_embeddings(input_file, output_index)

    with open(output_index, 'rb') as f:
        texts, embeddings = pickle.load(f)
    assert len(texts) == 2
