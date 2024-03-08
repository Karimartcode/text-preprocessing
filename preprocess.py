import re


def load_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def tokenize_words(text):
    return text.split()


def tokenize_sentences(text):
    return re.split(r'(?<=[.!?])\s+', text)
