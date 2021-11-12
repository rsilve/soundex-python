"""Soundex game."""
import re

PREVIOUS_MATCH = "\\g<1>"
EMPTY_CHAR = "0000"


def encode_soundex_word(word: str) -> str:
    """Encode the parameter with soundex algorithm."""
    if not word:
        return EMPTY_CHAR
    word = word.upper()
    letters = _ignore_non_letter_char(word)
    if not letters:
        return EMPTY_CHAR
    first = _extract_first_char(letters)
    encoded = first
    if len(letters) > 1:
        numbered = _map_consonant_to_number(letters)
        cleaned = _remove_h_w_y(numbered)
        cleaned = _remove_adjacent_number(cleaned)
        cleaned = _remove_vowels(cleaned)
        encoded = f"{first}{cleaned[1:]}"
    padded = _pads_zero(encoded)
    truncated = _truncate(padded)
    return truncated


def _truncate(word: str) -> str:
    """Keep only the 4 first char."""
    return word[0:4]


def _remove_vowels(word: str) -> str:
    """Remove vowels from the word (not if in first position)."""
    return re.sub("(.)[AEIOU]", PREVIOUS_MATCH, word)


def _remove_h_w_y(word: str) -> str:
    """Remove the letters H W Y."""
    return re.sub("(.)[HWY]", PREVIOUS_MATCH, word)


def _remove_adjacent_number(word: str) -> str:
    """Keep only one number if two adjacent identical number."""
    return re.sub("(\\d)\\1+", PREVIOUS_MATCH, word)


def _map_consonant_to_number(word: str) -> str:
    """Replace letters by number."""
    word = re.sub(r"[BFPV]", "1", word)
    word = re.sub(r"[CGJKQSXZ]", "2", word)
    word = re.sub(r"[DT]", "3", word)
    word = re.sub(r"[L]", "4", word)
    word = re.sub(r"[MN]", "5", word)
    word = re.sub(r"[R]", "6", word)
    return word


def _ignore_non_letter_char(word: str) -> str:
    """Keep only letters."""
    return re.sub("[^A-Z]", "", word)


def _pads_zero(word: str) -> str:
    """Add zeros on the right to have at least 4 characters."""
    diff = 4 - len(word)
    if diff > 0:
        return word.ljust(4, "0")
    else:
        return word


def _extract_first_char(word: str) -> str:
    """Extract the first char of the word."""
    head = word[0]
    return head
