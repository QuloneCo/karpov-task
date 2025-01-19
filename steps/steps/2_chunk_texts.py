def chunk_texts(input_file, output_file, chunk_size=500):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    
    with open(output_file, 'w', encoding='utf-8') as out:
        for chunk in chunks:
            out.write(chunk + '\n---\n')
    print(f"Тексты разбиты на чанки и сохранены в {output_file}")

