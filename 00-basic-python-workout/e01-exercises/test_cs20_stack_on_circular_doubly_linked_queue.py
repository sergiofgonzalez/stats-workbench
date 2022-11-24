import unittest
from cs20_stack_on_circular_doubly_linked_list import Stack
# to get the coverage reports install coverage package using `conda install coverage` (if not already there) and run:
# + `coverage run <name-of-the-file.py>
# + `coverage report` &mdash; text report
# + `coverage html` &mdash; html report


class TestStackOnCircularDoublyLinkedList(unittest.TestCase):

    def test_initialize_stack(self):
        s = Stack()

        self.assertTrue(s.is_empty())
        self.assertEqual(len(s), 0)
        self.assertEqual(str(s), "-- empty stack --")

    def test_pop_from_empty_stack_fails(self):
        s = Stack()

        with self.assertRaises(Exception):
            s.pop()

    def test_peek_from_empty_stack_fails(self):
        s = Stack()

        with self.assertRaises(Exception):
            s.peek()

    def test_push_one_elem(self):
        s = Stack()

        s.push('a')
        self.assertFalse(s.is_empty())
        self.assertEqual(len(s), 1)
        self.assertEqual(str(s), "0: a")

    def test_pop_from_one_elem_stack(self):
        s = Stack()
        s.push('a')

        elem = s.pop()

        self.assertTrue(s.is_empty())
        self.assertEqual(elem, 'a')

    def test_peek_from_one_elem_stack(self):
        s = Stack()
        s.push('a')

        elem = s.peek()

        self.assertFalse(s.is_empty())
        self.assertEqual(len(s), 1)
        self.assertEqual(elem, 'a')

    def test_push_two_elems(self):
        s = Stack()

        s.push('b')
        s.push('a')

        self.assertFalse(s.is_empty())
        self.assertEqual(len(s), 2)
        self.assertEqual(str(s), "1: b\n0: a")

    def test_peek_in_two_elems_stack(self):
        s = Stack()
        s.push('b')
        s.push('a')

        top_of_stack = s.peek()

        self.assertFalse(s.is_empty())
        self.assertEqual(len(s), 2)
        self.assertEqual(str(s), "1: b\n0: a")
        self.assertEqual(top_of_stack, 'a')

    def test_pop_from_two_elems_stack(self):
        s = Stack()
        s.push('b')
        s.push('a')

        top_of_stack = s.pop()

        self.assertFalse(s.is_empty())
        self.assertEqual(len(s), 1)
        self.assertEqual(str(s), "0: b")
        self.assertEqual(top_of_stack, 'a')

    def test_pop_twice_from_two_elems_stack(self):
        s = Stack()
        s.push('b')
        s.push('a')

        top_1 = s.pop()
        top_2 = s.pop()

        self.assertTrue(s.is_empty())
        self.assertEqual(len(s), 0)
        self.assertEqual(str(s), "-- empty stack --")
        self.assertEqual(top_1, 'a')
        self.assertEqual(top_2, 'b')

    def test_pop_twice_then_push(self):
        s = Stack()
        s.push('b')
        s.push('a')

        top_1 = s.pop()
        top_2 = s.pop()
        s.push('c')

        self.assertFalse(s.is_empty())
        self.assertEqual(len(s), 1)
        self.assertEqual(str(s), "0: c")


if __name__ == "__main__":
    unittest.main()
