import unittest
from more_functions import validate_input_in_functions as val_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual('python1!: 0', val_input.score_input('python1!'))

    def test_score_input_test_score_valid(self):
        self.assertEqual('python2: 97', val_input.score_input('python2', 97))

    def test_score_input_test_score_below_range(self):
        self.assertEqual('invalid test score, please try again', val_input.score_input('python3', -1))

    def test_score_input_test_score_above_range(self):
        self.assertEqual('invalid test score, please try again', val_input.score_input('python4', 101))

    def test_test_score_non_numeric(self):
        with self.assertRaises(TypeError):
            val_input.score_input('python5', 'fifty')

    def test_score_input_invalid_message(self):
        self.assertEqual('invalid test score, please try again', val_input.score_input('python6', 101, 'invalid test score, please try again'))

