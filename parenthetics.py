"""Parenthetics module."""
from dll import dll


def parenthetics(string):
    """Module checks for open sets."""
    matches = link_list()
    for character in string:
        if character == "(":
            matches.append(character)
        if character == ")":
            if matches.head is None or matches.pop() != "(":
                return -1
    if matches.head is None:
        return 0
    else:
        return 1
