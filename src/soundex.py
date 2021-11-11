import re

PREVIOUS_MATCH = "\\g<1>"
EMPTY_CHAR = '0000'


def encode(word: str) -> str:
    if not word:
        return EMPTY_CHAR
    word = word.upper()
    letters = ignore_non_letter_char(word)
    if not letters:
        return EMPTY_CHAR
    first = extract_first_char(letters)
    encoded = first
    if len(letters) > 1:
        numbered = map_consonant_to_number(letters)
        cleaned = remove_h_w_y(numbered)
        cleaned = remove_adjacent_number(cleaned)
        cleaned = remove_vowels(cleaned)
        encoded = f'{first}{cleaned[1:]}'
    padded = pads_zero(encoded)
    truncated = truncate(padded)
    return truncated


def truncate(word: str) -> str:
    return word[0:4]


def remove_vowels(word: str) -> str:
    return re.sub('(.)[AEIOU]', PREVIOUS_MATCH, word)


def remove_h_w_y(word: str) -> str:
    return re.sub('(.)[HWY]', PREVIOUS_MATCH, word)


def remove_adjacent_number(word: str) -> str:
    return re.sub('(\\d)\\1+', PREVIOUS_MATCH, word)


def map_consonant_to_number(word: str) -> str:
    word = re.sub(r"[BFPV]", '1', word)
    word = re.sub(r"[CGJKQSXZ]", '2', word)
    word = re.sub(r"[DT]", '3', word)
    word = re.sub(r"[L]", '4', word)
    word = re.sub(r"[MN]", '5', word)
    word = re.sub(r"[R]", '6', word)
    return word


def ignore_non_letter_char(word: str) -> str:
    return re.sub('[^A-Z]', '', word)


def pads_zero(word: str) -> str:
    diff = 4 - len(word)
    if diff > 0:
        return word.ljust(4, '0')
    else:
        return word


def extract_first_char(word: str) -> str:
    head = word[0]
    return head
