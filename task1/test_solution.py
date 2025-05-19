import unittest

from task1.solution import sum_two


class TestStrictDecorator(unittest.TestCase):
    def test_correct_types(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_float_second_argument(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.5)

    def test_str_second_argument(self):
        with self.assertRaises(TypeError):
            sum_two(1, "2")

    def test_bool_second_argument(self):
        with self.assertRaises(TypeError):
            sum_two(1, True)

    def test_keyword_arguments(self):
        with self.assertRaises(TypeError):
            sum_two(a=1, b="2")


if __name__ == "__main__":
    unittest.main()