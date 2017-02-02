# -*- coding: utf-8 -*-
from trie import Trie


class AutoComplete(object): # class
    """Python implementation of autocomplete class."""
    def __init__(self, vocabulary, max_completions=5): # initialise newly created object
        """Initialize the Autocomplete class."""
        self.vocabulary = Trie(iterable=vocabulary)
        self.max_completions = max_completions

    def __call__(self, token): #method in the meta-class allows the class's instance to be called as a function
        """Takes user input and returns list of words, max five."""
        suggested_words = []
        if not isinstance(token, str):
            return suggested_words
        start = self.vocabulary.root
        token = token
        completions = 0
        while completions < self.max_completions: # loop
            while True:
                if start.keys()[0] != '#':
                    start, token = get_word(start, token)
                else:
                    suggested_words.append(token)
                    break #break loop
            return suggested_words

def get_word(start, token):
    k = start.keys()[0]
    token += k
    start = start[k]
    return start, token
