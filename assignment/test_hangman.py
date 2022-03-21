import unittest
from unittest import skip

from hangman_words import word_list
from hangman import pick_a_word, process_guess, single_letter_guess, whole_word_guess, get_word_to_display, \
    all_letters_guessed, display_hangman


class TestHangman(unittest.TestCase):
    def setUp(self) -> None:
        self.word = pick_a_word()
        self.correct_guess = self.word

    def test_wordlist_returns_list_of_words(self):
        self.assertIsNotNone(self.word)
        self.assertTrue(len(self.word) > 1)

    def test_pick_a_word_returns_word_in_list(self):
        self.assertIn(self.word, word_list)

    def test_word_or_blanks_to_display_has_valid_length(self):
        expected_word_to_display = "_" * len(self.word)
        actual_word_to_display = get_word_to_display(self.word)
        self.assertEqual(len(expected_word_to_display), len(actual_word_to_display))

    def test_all_letters_guessed_is_valid(self):
        whole_word_guess('wrong guess', self.word)
        self.assertFalse(all_letters_guessed(self.word))
        whole_word_guess(self.correct_guess, self.word)
        self.assertTrue(all_letters_guessed(self.word))

    def test_whole_word_guess_returns_true(self):
        self.assertFalse(whole_word_guess("wrong guess", self.word))
        self.assertTrue(whole_word_guess(self.correct_guess, self.word))

    def test_single_letter_guess_is_valid(self):
        for letter in self.correct_guess:
            single_letter_guess(letter, self.word)
        self.assertTrue(all_letters_guessed(self.word))

    def test_process_guess_is_valid(self):
        self.assertTrue(process_guess(self.correct_guess, self.word))
        with self.assertRaises(ValueError):
            process_guess("", self.word)

    def test_hangman_drawn_based_on_lives_remaining_is_valid(self):
        lives_lost_hangman = """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """
        lives_started_hangman = """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
        self.assertEqual(lives_started_hangman, display_hangman(6))
        self.assertEqual(lives_lost_hangman, display_hangman(0))
