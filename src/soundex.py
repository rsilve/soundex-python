import re

PREVIOUS_MATCH = "\\g<1>"
EMPTY_CHAR = "0000"


def encode(word: str) -> str:
    """
    encode the parameter with soundex algorithm
    :param word:
    :return: encoded string
    """
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
        encoded = f"{first}{cleaned[1:]}"
    padded = pads_zero(encoded)
    truncated = truncate(padded)
    return truncated


def truncate(word: str) -> str:
    """
    keep only the 4 first char
    :param word:
    :return: string truncated to 4 char
    """
    return word[0:4]


def remove_vowels(word: str) -> str:
    """
    remove vowels from the word (not if in first position)
    :param word:
    :return: the word without vowels
    """
    return re.sub("(.)[AEIOU]", PREVIOUS_MATCH, word)


def remove_h_w_y(word: str) -> str:
    """
    Remove the letters H W Y
    :param word:
    :return:
    """
    return re.sub("(.)[HWY]", PREVIOUS_MATCH, word)


def remove_adjacent_number(word: str) -> str:
    """
    keep only one number if two adjacent identical number
    :param word:
    :return: the word without indentical adjacent number
    """
    return re.sub("(\\d)\\1+", PREVIOUS_MATCH, word)


def map_consonant_to_number(word: str) -> str:
    """
    replace letters by number
    :param word:
    :return: word transformed
    """
    word = re.sub(r"[BFPV]", "1", word)
    word = re.sub(r"[CGJKQSXZ]", "2", word)
    word = re.sub(r"[DT]", "3", word)
    word = re.sub(r"[L]", "4", word)
    word = re.sub(r"[MN]", "5", word)
    word = re.sub(r"[R]", "6", word)
    return word


def ignore_non_letter_char(word: str) -> str:
    """
    keep only letters
    :param word:
    :return: word with only letters
    """
    return re.sub("[^A-Z]", "", word)


def pads_zero(word: str) -> str:
    """
    Add zeros on the right to have at least 4 characters
    :param word:
    :return: zero padded word
    """
    diff = 4 - len(word)
    if diff > 0:
        return word.ljust(4, "0")
    else:
        return word


def extract_first_char(word: str) -> str:
    """
    extract the first char of the word
    :param word:
    :return: the first char
    """
    head = word[0]
    return head
