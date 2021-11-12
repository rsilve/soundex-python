from unittest import TestCase

from src.soundex import encode_soundex_word


class Test(TestCase):
    def test_soundex(self):
        res = encode_soundex_word("r")
        self.assertEqual(res, "R000")
        res = encode_soundex_word("robert")
        self.assertEqual(res, "R163")
        res = encode_soundex_word("robbert")
        self.assertEqual(res, "R163")
        res = encode_soundex_word("")
        self.assertEqual(res, "0000")
        res = encode_soundex_word("Honeyman")
        self.assertEqual(res, "H555")
        res = encode_soundex_word("Rupert")
        self.assertEqual(res, "R163")
        res = encode_soundex_word("Ashcraft")
        self.assertEqual(res, "A261")
        res = encode_soundex_word("Tymczak")
        self.assertEqual(res, "T522")

    def test_retain_first_letter(self):
        res = encode_soundex_word("r")
        self.assertEqual(res[0], "R")
        res = encode_soundex_word("")
        self.assertEqual(res[0], "0")
        res = encode_soundex_word("robert")
        self.assertEqual(res[0], "R")
        res = encode_soundex_word("robbert")
        self.assertEqual(res[0], "R")
        res = encode_soundex_word("Honeyman")
        self.assertEqual(res[0], "H")
        res = encode_soundex_word("Rupert")
        self.assertEqual(res[0], "R")
        res = encode_soundex_word("Ashcraft")
        self.assertEqual(res[0], "A")
        res = encode_soundex_word("T")
        self.assertEqual(res[0], "T")

    def test_zero_padding(self):
        res = encode_soundex_word("r")
        self.assertEqual(res, "R000")

    def test_ignore_non_letter_char(self):
        res = encode_soundex_word("r1234")
        self.assertEqual(res, "R000")
        res = encode_soundex_word("1234")
        self.assertEqual(res, "0000")

    def test_map_consonant_to_number(self):
        res = encode_soundex_word("rtvn")
        self.assertEqual(res, "R315")

    def test_remove_adjacent_number(self):
        res = encode_soundex_word("rtdn")
        self.assertEqual(res, "R350")

    def test_clean_first_letter(self):
        res = encode_soundex_word("cgtn")
        self.assertEqual(res, "C350")

    def test_remove_separated_by_h(self):
        res = encode_soundex_word("rthd")
        self.assertEqual(res, "R300")
        res = encode_soundex_word("hcwq")
        self.assertEqual(res, "H200")

    def test_remove_separated_by_vowels(self):
        res = encode_soundex_word("rtac")
        self.assertEqual(res, "R320")
        res = encode_soundex_word("hetc")
        self.assertEqual(res, "H320")

    def test_truncate(self):
        res = encode_soundex_word("Ashcraft")
        self.assertEqual(res, "A261")
