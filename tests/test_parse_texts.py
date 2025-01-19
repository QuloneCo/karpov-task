import os
from steps.1_parse_texts import parse_texts

def test_parse_texts(tmp_path):
    input_dir = tmp_path / "input"
    input_dir.mkdir()
    (input_dir / "file1.txt").write_text("Hello world!")
    (input_dir / "file2.txt").write_text("Python is great!")

    output_file = tmp_path / "output.txt"
    parse_texts(input_dir, output_file)

    result = output_file.read_text()
    assert "Hello world!" in result
    assert "Python is great!" in result

