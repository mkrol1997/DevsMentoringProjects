from typing import Dict


def is_vowel(char: str) -> bool:
    """
    Checks if a given character is a vowel.
    """
    vowels = 'aeiouy'
    return char.lower() in vowels


def count_vowels(text: str, result: dict) -> Dict[str, int]:
    """
    Recursively counts the occurrences of each vowel in the given text and updates the results in a dictionary.
    """
    if not text:
        return result

    if is_vowel(text[0]):
        try:
            result[text[0]] += 1
        except KeyError:
            result[text[0]] = 1

    return count_vowels(text[1:], result)
