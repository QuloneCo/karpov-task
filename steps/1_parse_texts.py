import os

def parse_texts(input_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as out:
        for filename in os.listdir(input_dir):
            if filename.endswith('.txt'):
                with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as f:
                    out.write(f.read() + '\n')
    print(f"Тексты из {input_dir} сохранены в {output_file}")
