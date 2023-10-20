import re


def load_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
