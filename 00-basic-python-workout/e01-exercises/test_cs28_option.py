import unittest
from cs28_option import Some, Empty, wrap
# to get the coverage reports install coverage package using `conda install coverage` (if not already there) and run:
# + `coverage run <name-of-the-file.py>
# + `coverage report` &mdash; text report
# + `coverage html` &mdash; html report


class TestOption(unittest.TestCase):

    def test_get_or_else_uses_value_for_some_and_alt_for_empty(self):
        names = (Some("Jason"), Empty(), Some("Isaacs"))
        expected = ("Jason", "Unknown!", "Isaacs")

        for i in range(len(names)):
            name = names[i]
            value = name.get_or_else("Unknown!")
            self.assertEqual(expected[i], value)

    def test_has_next_with_get_uses_only_values_for_somes(self):
        names = (Some("Jason"), Empty(), Some("Isaacs"))
        expected = ("Jason", "Unknown!", "Isaacs")
        for i in range(len(names)):
            name = names[i]
            if name.has_value():
                value = name.get()
                self.assertEqual(expected[i], value)

    def test_method_returning_option(self):
        option_1 = wrap("Hello")
        self.assertEqual(str(option_1), "Some(Hello)")
        self.assertTrue(isinstance(option_1, Some))
        self.assertEqual(option_1.get(), "Hello")

        option_2 = wrap(None)
        self.assertEqual(str(option_2), "Empty()")
        self.assertTrue(isinstance(option_2, Empty))
        self.assertEqual(option_2.get_or_else("==empty=="), "==empty==")


if __name__ == "__main__":
    unittest.main()
