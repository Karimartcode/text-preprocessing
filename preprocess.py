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


STOPWORDS = set([
    'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
    'should', 'may', 'might', 'can', 'shall', 'to', 'of', 'in', 'for',
    'on', 'with', 'at', 'by', 'from', 'as', 'into', 'through', 'during',
    'before', 'after', 'and', 'but', 'or', 'nor', 'not', 'so', 'yet',
    'both', 'either', 'neither', 'each', 'every', 'all', 'any', 'few',
    'more', 'most', 'other', 'some', 'such', 'no', 'only', 'own', 'same',
    'than', 'too', 'very', 'just', 'because', 'if', 'when', 'where',
    'how', 'what', 'which', 'who', 'whom', 'this', 'that', 'these',
    'those', 'i', 'me', 'my', 'we', 'our', 'you', 'your', 'he', 'him',
    'his', 'she', 'her', 'it', 'its', 'they', 'them', 'their',
])

def remove_stopwords(tokens):
    return [t for t in tokens if t.lower() not in STOPWORDS]


SUFFIX_MAP = {
    'ing': '', 'tion': 'te', 'sion': 'de', 'ness': '',
    'ment': '', 'able': '', 'ible': '', 'ful': '',
    'less': '', 'ous': '', 'ive': '', 'ly': '',
    'er': '', 'est': '', 'ed': '', 'es': '', 's': ''
}

def simple_stem(word):
    for suffix, replacement in sorted(SUFFIX_MAP.items(), key=lambda x: -len(x[0])):
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            return word[:-len(suffix)] + replacement
    return word


def stem_tokens(tokens):
    return [simple_stem(t) for t in tokens]


def ngrams(tokens, n):
    return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]


from collections import Counter

def word_frequency(tokens):
    return Counter(tokens)


def build_vocabulary(texts):
    vocab = set()
    for text in texts:
        tokens = tokenize_words(text.lower())
        tokens = remove_punctuation(tokens)
        vocab.update(tokens)
    return sorted(vocab)


import numpy as np


def compute_tf(tokens):
    freq = word_frequency(tokens)
    total = len(tokens)
    return {word: count / total for word, count in freq.items()}


def compute_idf(documents):
    n = len(documents)
    idf = {}
    all_words = set()
    for doc in documents:
        all_words.update(set(doc))
    for word in all_words:
        df = sum(1 for doc in documents if word in set(doc))
        idf[word] = np.log(n / (1 + df))
    return idf


def compute_tfidf(documents):
    idf = compute_idf(documents)
    tfidf_docs = []
    for doc in documents:
        tf = compute_tf(doc)
        tfidf = {word: tf_val * idf.get(word, 0) for word, tf_val in tf.items()}
        tfidf_docs.append(tfidf)
    return tfidf_docs
