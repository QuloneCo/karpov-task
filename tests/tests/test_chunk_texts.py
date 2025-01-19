from steps.2_chunk_texts import chunk_texts

def test_chunk_texts(tmp_path):
    input_file = tmp_path / "input.txt"
    input_file.write_text("a" * 1000)
    
    output_file = tmp_path / "output.txt"
    chunk_texts(input_file, output_file, chunk_size=300)
    
    result = output_file.read_text()
    assert len(result.split('\n---\n')) == 4
