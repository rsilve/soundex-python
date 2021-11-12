from unittest import TestCase

from src import soundex


class Test(TestCase):

    def test_soundex(self):
        res = soundex.encode("r")
        self.assertEqual(res, "R000")
        res = soundex.encode("robert")
        self.assertEqual(res, "R163")
        res = soundex.encode("robbert")
        self.assertEqual(res, "R163")
        res = soundex.encode("")
        self.assertEqual(res, '0000')
        res = soundex.encode("Honeyman")
        self.assertEqual(res, 'H555')
        res = soundex.encode("Rupert")
        self.assertEqual(res, 'R163')
        res = soundex.encode("Ashcraft")
        self.assertEqual(res, 'A261')
        res = soundex.encode("Tymczak")
        self.assertEqual(res, 'T522')

    def test_retain_first_letter(self):
        res = soundex.encode("r")
        self.assertEqual(res[0], "R")
        res = soundex.encode("")
        self.assertEqual(res[0], "0")
        res = soundex.encode("robert")
        self.assertEqual(res[0], "R")
        res = soundex.encode("robbert")
        self.assertEqual(res[0], "R")
        res = soundex.encode("Honeyman")
        self.assertEqual(res[0], 'H')
        res = soundex.encode("Rupert")
        self.assertEqual(res[0], 'R')
        res = soundex.encode("Ashcraft")
        self.assertEqual(res[0], 'A')
        res = soundex.encode("T")
        self.assertEqual(res[0], 'T')

    def test_zero_padding(self):
        res = soundex.encode("r")
        self.assertEqual(res, "R000")

    def test_ignore_non_letter_char(self):
        res = soundex.encode("r1234")
        self.assertEqual(res, "R000")
        res = soundex.encode("1234")
        self.assertEqual(res, "0000")

    def test_map_consonant_to_number(self):
        res = soundex.encode("rtvn")
        self.assertEqual(res, "R315")

    def test_remove_adjacent_number(self):
        res = soundex.encode("rtdn")
        self.assertEqual(res, "R350")

    def test_clean_first_letter(self):
        res = soundex.encode("cgtn")
        self.assertEqual(res, "C350")

    def test_remove_separated_by_h(self):
        res = soundex.encode("rthd")
        self.assertEqual(res, "R300")
        res = soundex.encode("hcwq")
        self.assertEqual(res, "H200")

    def test_remove_separated_by_vowels(self):
        res = soundex.encode("rtac")
        self.assertEqual(res, "R320")
        res = soundex.encode("hetc")
        self.assertEqual(res, "H320")

    def test_truncate(self):
        res = soundex.encode("Ashcraft")
        self.assertEqual(res, 'A261')
