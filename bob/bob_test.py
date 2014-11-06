# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

import bob


class BobTests(unittest.TestCase):

    def test_stating_something(self):
        self.assertEqual(
            'Whatever.',
            bob.Bob('Tom-ay-to, tom-aaaah-to.').hey()
        )

    def test_shouting(self):
        self.assertEqual(
            'Whoa, chill out!',
            bob.Bob('WATCH OUT!').hey()
        )

    def test_asking_a_question(self):
        self.assertEqual(
            'Sure.',
            bob.Bob('Does this cryogenic chamber make me look fat?').hey()
        )

    def test_asking_a_numeric_question(self):
        self.assertEqual(
            'Sure.',
            bob.Bob('You are, what, like 15?').hey()
        )

    def test_talking_forcefully(self):
        self.assertEqual(
            'Whatever.',
            bob.Bob("Let's go make out behind the gym!").hey()
        )

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            'Whatever.',
            bob.Bob("It's OK if you don't want to go to the DMV.").hey()
        )

    def test_forceful_questions(self):
        self.assertEqual(
            'Whoa, chill out!',
            bob.Bob('WHAT THE HELL WERE YOU THINKING?').hey()
        )

    def test_shouting_numbers(self):
        self.assertEqual(
            'Whoa, chill out!', bob.Bob('1, 2, 3 GO!').hey()
        )

    def test_only_numbers(self):
        self.assertEqual(
            'Whatever.', bob.Bob('1, 2, 3').hey()
        )

    def test_question_with_only_numbers(self):
        self.assertEqual(
            'Sure.', bob.Bob('4?').hey()
        )

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            'Whoa, chill out!',
            bob.Bob('ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!').hey()
        )

    def test_shouting_with_umlauts(self):
        self.assertEqual(
            'Whoa, chill out!', bob.Bob('ÜMLÄÜTS!').hey()
        )

    def test_calmly_speaking_with_umlauts(self):
        self.assertEqual(
            'Whatever.', bob.Bob('ÜMLäÜTS!').hey()
        )

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual(
            'Whoa, chill out!', bob.Bob('I HATE YOU').hey()
        )

    def test_statement_containing_question_mark(self):
        self.assertEqual(
            'Whatever.', bob.Bob('Ending with ? means a question.').hey()
        )

    def test_prattling_on(self):
        self.assertEqual(
            'Sure.', bob.Bob("Wait! Hang on. Are you going to be OK?").hey()
        )

    def test_silence(self):
        self.assertEqual(
            'Fine. Be that way!', bob.Bob('').hey()
        )

    def test_prolonged_silence(self):
        self.assertEqual(
            'Fine. Be that way!', bob.Bob('    \t').hey()
        )

    def test_starts_with_whitespace(self):
        self.assertEqual(
            'Whatever.', bob.Bob('         hmmmmmmm...').hey()
        )

    def test_ends_with_whitespace(self):
        self.assertEqual(
            'Sure.', bob.Bob('What if we end with whitespace?   ').hey()
        )

if __name__ == '__main__':
    unittest.main()
