import unittest
from cs15_circular_list import CircularList

# to get the coverage reports install coverage package using `conda install coverage` (if not already there) and run:
# + `coverage run <name-of-the-file.py>
# + `coverage report` &mdash; text report
# + `coverage html` &mdash; html report


class TestHeapBackedLinkedList(unittest.TestCase):

    def test_initialize_list(self):
        cl = CircularList()

        self.assertTrue(cl.is_empty())
        self.assertEqual(len(cl), 0)
        self.assertEqual(str(cl), "[]")

    def test_remove_from_empty_list_fails(self):
        cl = CircularList()

        with self.assertRaises(Exception):
            cl.remove(0)

    def test_insert_first_elem_on_empty_list(self):
        cl = CircularList()

        cl.insert('a', 0)

        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 1)
        self.assertEqual(str(cl), "[a]")

    def test_insert_two_elems_in_first_pos(self):
        cl = CircularList()

        cl.insert('b', 0)
        cl.insert('a', 0)

        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 2)
        self.assertEqual(str(cl), "[a, b]")

    def test_insert_three_elems_in_first_pos(self):
        cl = CircularList()

        cl.insert('c', 0)
        cl.insert('b', 0)
        cl.insert('a', 0)

        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 3)
        self.assertEqual(str(cl), "[a, b, c]")

    def test_insert_two_elems_in_succession(self):
        cl = CircularList()

        cl.insert('a', 0)
        cl.insert('b', 1)

        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 2)
        self.assertEqual(str(cl), "[a, b]")

    def test_insert_three_elems_in_succession(self):
        cl = CircularList()

        cl.insert('a', 0)
        cl.insert('b', 1)
        cl.insert('c', 2)

        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 3)
        self.assertEqual(str(cl), "[a, b, c]")

    def test_insert_three_elems_not_in_succession(self):
        cl = CircularList()

        cl.insert('a', 0)
        cl.insert('c', 1)
        cl.insert('b', 1)

        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 3)
        self.assertEqual(str(cl), "[a, b, c]")

    def test_insert_5_elems_in_succession(self):
        cl = CircularList()

        cl.insert('a', len(cl))
        cl.insert('b', len(cl))
        cl.insert('c', len(cl))
        cl.insert('d', len(cl))
        cl.insert('e', len(cl))

        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 5)
        self.assertEqual(str(cl), "[a, b, c, d, e]")

    def test_insert_5_elems_not_in_succession(self):
        cl = CircularList()

        cl.insert('a', 0)
        cl.insert('e', 1)
        cl.insert('c', 1)
        cl.insert('b', 1)
        cl.insert('d', 3)

        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 5)
        self.assertEqual(str(cl), "[a, b, c, d, e]")

    def test_remove_elem_in_first_pos(self):
        cl = CircularList()
        cl.insert('a', 0)

        cl.remove(0)

        self.assertTrue(cl.is_empty())
        self.assertEqual(len(cl), 0)
        self.assertEqual(str(cl), "[]")

    def test_remove_elems_in_second_pos_from_list_with_two_elems(self):
        cl = CircularList()
        cl.insert('a', 0)
        cl.insert('b', 1)

        cl.remove(1)

        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 1)
        self.assertEqual(str(cl), "[a]")

    def test_remove_elems_in_last_pos(self):
        cl = CircularList()
        cl.insert('a', 0)
        cl.insert('b', 1)
        cl.insert('c', 2)
        cl.insert('d', 3)
        cl.insert('e', 4)

        cl.remove(len(cl) - 1)
        self.assertEqual(len(cl), 4)
        self.assertEqual(str(cl), "[a, b, c, d]")

        cl.remove(len(cl) - 1)
        self.assertEqual(len(cl), 3)
        self.assertEqual(str(cl), "[a, b, c]")

        cl.remove(len(cl) - 1)
        self.assertEqual(len(cl), 2)
        self.assertEqual(str(cl), "[a, b]")

        cl.remove(len(cl) - 1)
        self.assertEqual(len(cl), 1)
        self.assertEqual(str(cl), "[a]")

        cl.remove(len(cl) - 1)
        self.assertTrue(cl.is_empty())
        self.assertEqual(len(cl), 0)
        self.assertEqual(str(cl), "[]")

    def test_remove_elems_in_first_pos_from_list_with_two_elems(self):
        cl = CircularList()
        cl.insert('a', 0)
        cl.insert('b', 1)

        cl.remove(0)

        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 1)
        self.assertEqual(str(cl), "[b]")

    def test_remove_elems(self):
        cl = CircularList()
        cl.insert('a', 0)
        cl.insert('b', 1)
        cl.insert('c', 2)
        cl.insert('d', 3)
        cl.insert('e', 4)

        cl.remove(3)
        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 4)
        self.assertEqual(str(cl), "[a, b, c, e]")

        cl.remove(2)
        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 3)
        self.assertEqual(str(cl), "[a, b, e]")

        cl.remove(1)
        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 2)
        self.assertEqual(str(cl), "[a, e]")

        cl.remove(1)
        self.assertFalse(cl.is_empty())
        self.assertEqual(len(cl), 1)
        self.assertEqual(str(cl), "[a]")

        cl.remove(0)
        self.assertTrue(cl.is_empty())
        self.assertEqual(len(cl), 0)
        self.assertEqual(str(cl), "[]")

    def test_iter_is_circular(self):
        cl = CircularList()
        cl.insert('a', 0)
        cl.insert('b', 1)
        cl.insert('c', 2)
        cl.insert('d', 3)
        cl.insert('e', 4)

        tuples = list(zip(range(len(cl) + 2), cl))
        self.assertEqual(tuples[0], (0, 'a'))
        self.assertEqual(tuples[1], (1, 'b'))
        self.assertEqual(tuples[2], (2, 'c'))
        self.assertEqual(tuples[3], (3, 'd'))
        self.assertEqual(tuples[4], (4, 'e'))
        self.assertEqual(tuples[5], (5, 'a'))
        self.assertEqual(tuples[6], (6, 'b'))

    def test_iter_over_empty_circular_list(self):
        cl = CircularList()
        for elem in cl:
            ...

    def test_node_to_string(self):
        node = CircularList.Node('data', 'next')
        self.assertEqual(str(node), "(data=data, next=next)")


if __name__ == "__main__":
    unittest.main()
