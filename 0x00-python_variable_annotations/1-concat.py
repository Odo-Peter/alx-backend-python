#!/usr/bin/env python3
"""Write a type-annotated function concat"""


def concat(str1: str, str2: str) -> str:
    """Concatenates two strings

    Args:
        str1 (str): First string recieved via params
        str2 (str): Second string recieved via params

    Return:
        (str) - concatenated string
    """
    return ''.join([str1, str2])
