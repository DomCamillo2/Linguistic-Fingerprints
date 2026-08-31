import math

import spacy

from linguistic_fingerprints.features import (
    AUDIT_FEATURES,
    CONFIRMATORY_FEATURES,
    extract_text_features,
    moving_average_type_token_ratio,
)


def test_feature_inventory_is_frozen_at_fifteen_confirmatory_features():
    assert len(CONFIRMATORY_FEATURES) == 15
    assert set(CONFIRMATORY_FEATURES).isdisjoint(AUDIT_FEATURES)


def test_mattr_short_sequence_uses_available_length():
    assert moving_average_type_token_ratio(["a", "b", "a"], window=50) == 2 / 3


def test_empty_mattr_is_zero():
    assert moving_average_type_token_ratio([], window=50) == 0.0


def test_feature_extraction_is_finite_on_short_text():
    nlp = spacy.blank("en")
    nlp.add_pipe("sentencizer")
    text = "However, time passes. Time passes slowly."
    features = extract_text_features(nlp(text), text)

    assert features["n_sentences"] == 2
    assert features["n_words"] == 6
    assert features["sentence_initial_connective_prop"] == 0.5
    assert all(math.isfinite(value) for value in features.values())
