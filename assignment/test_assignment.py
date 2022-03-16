import unittest
from assignment import has_duplicates, missing_letters


class AssignmentTest(unittest.TestCase):
    def test_has_duplicates(self):
        has_dup = has_duplicates("jamess")
        self.assertTrue(has_dup, "Has Duplicate does not detect duplicates")

    def test_has_no_duplicates(self):
        has_dup = has_duplicates("james")
        self.assertFalse(has_dup, "Has duplicate detects duplicates when there are noe")

    def test_missing_letters(self):
        missing_l = missing_letters("zzz")
        self.assertEqual(missing_l, "abcdefghijklmnopqrstuvwxy")
        missing_l2 = missing_letters("the quick brown fox jumps over the lazy dog")
        self.assertEqual(missing_l2, "")
