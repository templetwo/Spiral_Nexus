from ingestion.parser import parse_scroll
from pathlib import Path

def test_parse_scroll_output_keys():
    scroll = parse_scroll(Path("tests/fixtures/sample_scroll.txt"))
    assert set(scroll.keys()) >= {"id", "content", "tone_vector", "glyph_sig", "visibility"}

def test_tone_vector_length():
    scroll = parse_scroll(Path("tests/fixtures/sample_scroll.txt"))
    assert len(scroll["tone_vector"]) == 6
