# -*- coding: utf-8 -*-
from trie import Trie


class AutoCompleter(object):
    """Python implementation of autocomplete class."""
    def __init__(self, vocabulary, max_completions=5):
        """Initialize the Autocompleter class."""
        self.vocabulary = Trie(iterable=vocabulary)
        self.max_completions = max_completions
