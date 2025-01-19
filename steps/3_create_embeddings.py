from sentence_transformers import SentenceTransformer
import pickle

def create_embeddings(input_file, output_index):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    with open(input_file, 'r', encoding='utf-8') as f:
        texts = f.read().split('\n---\n')
    
    embeddings = model.encode(texts)
    
    with open(output_index, 'wb') as f:
        pickle.dump((texts, embeddings), f)
    print(f"Индекс сохранён в {output_index}")
