import re
from pathlib import Path

def parse_scroll(file_path: Path) -> dict:
    text = file_path.read_text(encoding="utf-8")
    return {
        "id": file_path.stem,
        "content": text,
        "tone_vector": [0.5, 0.3, 0.2, 0.6, 0.4, 0.1],  # placeholder
        "glyph_sig": extract_glyph_signature(text),
        "visibility": guess_visibility(text),
    }

def extract_glyph_signature(text: str) -> dict:
    glyphs = ["🜁", "✱", "⟡", "⟁", "🜂", "†"]
    return {g: text.count(g) for g in glyphs if g in text}

def guess_visibility(text: str) -> str:
    if "🕯" in text:
        return "sacred"
    elif "🔒" in text:
        return "threshold"
    return "open"
