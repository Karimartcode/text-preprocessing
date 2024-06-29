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
