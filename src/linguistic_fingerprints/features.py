"""Transparent linguistic features for controlled LLM-response corpora."""

from __future__ import annotations

import re
from collections import Counter
from statistics import fmean, pstdev
from typing import Iterable, Sequence

from spacy.tokens import Doc, Token


MODALS = {
    "can",
    "could",
    "may",
    "might",
    "must",
    "shall",
    "should",
    "will",
    "would",
}

CONNECTIVES = {
    "additionally",
    "although",
    "consequently",
    "furthermore",
    "however",
    "moreover",
    "nevertheless",
    "otherwise",
    "therefore",
    "thus",
}

FUNCTION_UPOS = {"ADP", "AUX", "CCONJ", "DET", "PART", "PRON", "SCONJ"}
UPOS_TAGS = (
    "ADJ",
    "ADP",
    "ADV",
    "AUX",
    "CCONJ",
    "DET",
    "NOUN",
    "NUM",
    "PART",
    "PRON",
    "PROPN",
    "SCONJ",
    "VERB",
)

AUDIT_FEATURES = (
    "n_surface_tokens",
    "n_words",
    "raw_ttr",
)

CONFIRMATORY_FEATURES = (
    "n_sentences",
    "mean_word_chars",
    "mean_sentence_words",
    "sd_sentence_words",
    "mattr_50",
    "repeated_token_rate",
    "repeated_bigram_rate",
    "function_word_prop",
    "modal_prop",
    "connective_prop",
    "punctuation_prop",
    "adjacent_sentence_lexical_overlap",
    "upos_ADJ_prop",
    "upos_NOUN_prop",
    "upos_VERB_prop",
)


def _safe_mean(values: Sequence[float]) -> float:
    return float(fmean(values)) if values else 0.0


def _safe_std(values: Sequence[float]) -> float:
    return float(pstdev(values)) if len(values) > 1 else 0.0


def _rate(count: int, denominator: int) -> float:
    return float(count / denominator) if denominator else 0.0


def moving_average_type_token_ratio(items: Sequence[str], window: int = 50) -> float:
    """Compute MATTR; use one all-token window when the text is shorter."""

    if not items:
        return 0.0
    window = max(1, min(window, len(items)))
    scores = [len(set(items[i : i + window])) / window for i in range(len(items) - window + 1)]
    return float(fmean(scores))


def _adjacent_sentence_overlap(sent_words: list[list[str]]) -> float:
    scores: list[float] = []
    for left, right in zip(sent_words, sent_words[1:]):
        left_set, right_set = set(left), set(right)
        union = left_set | right_set
        scores.append(len(left_set & right_set) / len(union) if union else 0.0)
    return _safe_mean(scores)


def _repeated_bigram_rate(words: Sequence[str]) -> float:
    bigrams = list(zip(words, words[1:]))
    if not bigrams:
        return 0.0
    counts = Counter(bigrams)
    repeated_occurrences = sum(count for count in counts.values() if count > 1)
    return repeated_occurrences / len(bigrams)


def _sentence_words(doc: Doc) -> list[list[str]]:
    sentences: list[list[str]] = []
    try:
        spans: Iterable = doc.sents
        for sent in spans:
            words = [token.lower_ for token in sent if token.is_alpha]
            if words:
                sentences.append(words)
    except ValueError:
        words = [token.lower_ for token in doc if token.is_alpha]
        if words:
            sentences.append(words)
    return sentences


def _lemma(token: Token) -> str:
    lemma = token.lemma_.strip().lower()
    return lemma if lemma else token.lower_


def extract_text_features(doc: Doc, raw_text: str, mattr_window: int = 50) -> dict[str, float]:
    """Extract a deterministic, interpretable feature dictionary from one SpaCy doc."""

    surface_tokens = [token for token in doc if not token.is_space]
    words = [token for token in doc if token.is_alpha]
    lower_words = [token.lower_ for token in words]
    lemmas = [_lemma(token) for token in words]
    sentence_words = _sentence_words(doc)
    sentence_lengths = [len(sentence) for sentence in sentence_words]

    pos_counts = Counter(token.pos_ for token in words if token.pos_)
    paragraph_count = len([part for part in re.split(r"\n\s*\n", raw_text.strip()) if part])
    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
    list_lines = sum(bool(re.match(r"^(?:[-*•]|\d+[.)])\s+", line)) for line in lines)
    heading_lines = sum(line.startswith("#") for line in lines)

    sentence_initials = [sentence[0] for sentence in sentence_words if sentence]
    modal_count = sum(word in MODALS for word in lower_words)
    connective_count = sum(word in CONNECTIVES for word in lower_words)
    function_word_count = sum(token.pos_ in FUNCTION_UPOS for token in words)

    features: dict[str, float] = {
        "n_surface_tokens": float(len(surface_tokens)),
        "n_words": float(len(words)),
        "n_sentences": float(len(sentence_words)),
        "n_paragraphs": float(paragraph_count),
        "mean_word_chars": _safe_mean([len(token.text) for token in words]),
        "mean_sentence_words": _safe_mean(sentence_lengths),
        "sd_sentence_words": _safe_std(sentence_lengths),
        "mattr_50": moving_average_type_token_ratio(lemmas, mattr_window),
        "raw_ttr": _rate(len(set(lemmas)), len(lemmas)),
        "repeated_token_rate": _rate(len(lower_words) - len(set(lower_words)), len(lower_words)),
        "repeated_bigram_rate": _repeated_bigram_rate(lower_words),
        "function_word_prop": _rate(function_word_count, len(words)),
        "modal_prop": _rate(modal_count, len(words)),
        "connective_prop": _rate(connective_count, len(words)),
        "sentence_initial_connective_prop": _rate(
            sum(word in CONNECTIVES for word in sentence_initials), len(sentence_initials)
        ),
        "punctuation_prop": _rate(sum(token.is_punct for token in surface_tokens), len(surface_tokens)),
        "apostrophe_word_prop": _rate(sum("'" in token.text or "’" in token.text for token in words), len(words)),
        "list_line_prop": _rate(list_lines, len(lines)),
        "heading_line_prop": _rate(heading_lines, len(lines)),
        "adjacent_sentence_lexical_overlap": _adjacent_sentence_overlap(sentence_words),
    }

    for tag in UPOS_TAGS:
        features[f"upos_{tag}_prop"] = _rate(pos_counts[tag], len(words))

    return features
