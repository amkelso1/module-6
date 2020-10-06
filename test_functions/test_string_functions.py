import unittest
from more_functions import string_functions


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(string_functions.multiply_string('alex', 7))


if __name__ == '__main__':
    unittest.main()
