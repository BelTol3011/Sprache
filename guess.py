from base import *


def conjugate_verb(word_stem: str, number: str, person: str) -> str:
    """Conjugates a verb"""
    return word_stem + verb_suffixes[number][person]


def get_verb_word_stem(verb: str) -> str:
    """Returns the word stem of a given verb"""
    for suffix in verb_suffixes_list:
        if verb.endswith(suffix):
            return verb[:-len(suffix)]

    return verb
