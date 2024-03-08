import re


def load_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def tokenize_words(text):
    return text.split()


def tokenize_sentences(text):
    return re.split(r'(?<=[.!?])\s+', text)


def to_lowercase(tokens):
    return [t.lower() for t in tokens]


def remove_punctuation(tokens):
    return [re.sub(r'[^\w\s]', '', t) for t in tokens if re.sub(r'[^\w\s]', '', t)]


def remove_numbers(tokens):
    return [t for t in tokens if not t.isdigit()]


def remove_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()
