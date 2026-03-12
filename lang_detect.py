from collections import Counter


# Common stopwords as a proxy for language detection
_STOPWORDS = {
    "en": {"the", "is", "in", "and", "to", "of", "a", "that", "it", "was"},
    "fr": {"le", "la", "les", "de", "du", "en", "et", "est", "un", "une"},
    "es": {"el", "la", "los", "de", "en", "y", "es", "un", "una", "que"},
}


def detect_language(text: str) -> str:
    """Heuristic language detection based on stopword frequency."""
    words = set(text.lower().split())
    scores = {
        lang: len(words & stops)
        for lang, stops in _STOPWORDS.items()
    }
    return max(scores, key=scores.get)
