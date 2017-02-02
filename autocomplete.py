# -*- coding: utf-8 -*-
from trie import Trie


class AutoComplete(object):
    """Python implementation of autocomplete class."""
    def __init__(self, vocabulary, max_completions=5):
        """Initialize the Autocomplete class."""
        self.vocabulary = Trie(iterable=vocabulary)
        self.max_completions = max_completions

    def __call__(self, token):
        """Takes user input and returns list of words, max five."""
        suggested_words = []
        if not isinstance(token, str):
            return suggested_words
        start = self.vocabulary.root
        token = token
        completions = 0
        while completions < self.max_completions:
            while True:
                if start.keys()[0] != '#':
                    start, token = get_word(start, token)
                else:
                    suggested_words.append(token)
                    break
            return suggested_words
