import unittest
from cs18_doubly_linked_list import DoublyLinkedList
# to get the coverage reports install coverage package using `conda install coverage` (if not already there) and run:
# + `coverage run <name-of-the-file.py>
# + `coverage report` &mdash; text report
# + `coverage html` &mdash; html report


class TestDoublyLinkedList(unittest.TestCase):

    def test_queue_can_be_created(self):
        ll = DoublyLinkedList()

        self.assertTrue(ll.is_empty())
        self.assertEqual(len(ll), 0)
        self.assertEqual(str(ll), "[]")

    def test_insert_first_elem_below_zero(self):
        ll = DoublyLinkedList()

        with self.assertRaises(Exception):
            ll.insert('a', -1)

    def test_insert_first_elem_beyond_zero(self):
        ll = DoublyLinkedList()

        with self.assertRaises(Exception):
            ll.insert('a', 1)

    def test_insert_first_elem(self):
        ll = DoublyLinkedList()

        ll.insert('a', 0)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 1)
        self.assertEqual(str(ll), "[a]")

    def test_insert_second_elem_beyond_len(self):
        ll = DoublyLinkedList()

        ll.insert('a', 0)

        with self.assertRaises(Exception):
            ll.insert('b', len(ll) + 1)

    def test_insert_as_first_in_two_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('b', 0)

        ll.insert('a', 0)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 2)
        self.assertEqual(str(ll), "[a, b]")

    def test_insert_as_second_in_two_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('a', 0)

        ll.insert('b', 1)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 2)
        self.assertEqual(str(ll), "[a, b]")

    def test_insert_before_first_in_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('b', 0)
        ll.insert('e', 1)
        ll.insert('h', 2)

        ll.insert('a', 0)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 4)
        self.assertEqual(str(ll), "[a, b, e, h]")

    def test_insert_before_second_in_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('b', 0)
        ll.insert('e', 1)
        ll.insert('h', 2)

        ll.insert('c', 1)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 4)
        self.assertEqual(str(ll), "[b, c, e, h]")

    def test_insert_before_third_in_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('b', 0)
        ll.insert('e', 1)
        ll.insert('h', 2)

        ll.insert('f', 2)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 4)
        self.assertEqual(str(ll), "[b, e, f, h]")

    def test_insert_after_third_in_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('b', 0)
        ll.insert('e', 1)
        ll.insert('h', 2)

        ll.insert('k', 3)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 4)
        self.assertEqual(str(ll), "[b, e, h, k]")

    def test_remove_below_bounds_fails(self):
        ll = DoublyLinkedList()

        with self.assertRaises(Exception):
            ll.remove(-1)

    def test_remove_on_empty_list_fails(self):
        ll = DoublyLinkedList()

        with self.assertRaises(Exception):
            ll.remove(0)

    def test_remove_beyond_bound_fails(self):
        ll = DoublyLinkedList()
        ll.insert('a', 0)

        with self.assertRaises(Exception):
            ll.remove(1)

    def test_remove_elem_from_list_one_elem(self):
        ll = DoublyLinkedList()
        ll.insert('a', 0)

        ll.remove(0)

        self.assertTrue(ll.is_empty())
        self.assertEqual(len(ll), 0)
        self.assertEqual(str(ll), "[]")

    def test_remove_first_elem_from_two_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)

        ll.remove(0)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 1)
        self.assertEqual(str(ll), "[b]")

    def test_remove_second_elem_from_two_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)

        ll.remove(1)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 1)
        self.assertEqual(str(ll), "[a]")

    def test_remove_first_elem_from_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)
        ll.insert('c', 2)

        ll.remove(0)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 2)
        self.assertEqual(str(ll), "[b, c]")

    def test_remove_second_elem_from_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)
        ll.insert('c', 2)

        ll.remove(1)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 2)
        self.assertEqual(str(ll), "[a, c]")

    def test_remove_third_elem_from_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)
        ll.insert('c', 2)

        ll.remove(2)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 2)
        self.assertEqual(str(ll), "[a, b]")

    def test_find_by_pos_below_bounds_neg(self):
        ll = DoublyLinkedList()

        with self.assertRaises(Exception):
            ll.find_by_pos(-1)

    def test_find_by_pos_beyond_bounds_empty_list(self):
        ll = DoublyLinkedList()

        with self.assertRaises(Exception):
            ll.find_by_pos(0)

    def test_find_by_pos_beyond_bounds_non_empty(self):
        ll = DoublyLinkedList()
        ll.insert('a', 0)

        with self.assertRaises(Exception):
            ll.find_by_pos(1)

    def test_find_by_pos_first_elem_on_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('c', 0)
        ll.insert('b', 0)
        ll.insert('a', 0)

        node = ll.find_by_pos(0)

        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")
        self.assertEqual(node.data, "a")
        self.assertIsNone(node.prev)
        self.assertEqual(node.next.data, "b")
        self.assertEqual(node.next.prev.data, "a")

    def test_find_by_pos_second_elem_on_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('c', 0)
        ll.insert('b', 0)
        ll.insert('a', 0)

        node = ll.find_by_pos(1)

        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")
        self.assertEqual(node.data, "b")
        self.assertEqual(node.prev.data, "a")
        self.assertEqual(node.next.data, "c")
        self.assertEqual(node.next.prev.data, "b")

    def test_find_by_pos_third_elem_on_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('c', 0)
        ll.insert('b', 0)
        ll.insert('a', 0)

        node = ll.find_by_pos(2)

        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")
        self.assertEqual(node.data, "c")
        self.assertEqual(node.prev.data, "b")
        self.assertIsNone(node.next)
        self.assertEqual(node.prev.next.data, "c")

    def test_find_by_data_find_first_on_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('b', 0)
        ll.insert('c', 1)
        ll.insert('a', 0)

        node = ll.find_by_data('a')
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")
        self.assertEqual(node.data, "a")
        self.assertIsNone(node.prev)
        self.assertEqual(node.next.data, 'b')
        self.assertEqual(node.next.prev.data, 'a')

    def test_find_by_data_find_second_on_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('b', 0)
        ll.insert('c', 1)
        ll.insert('a', 0)

        node = ll.find_by_data('b')
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")
        self.assertEqual(node.data, "b")
        self.assertEqual(node.prev.data, "a")
        self.assertEqual(node.next.data, "c")

    def test_find_by_data_find_third_on_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('b', 0)
        ll.insert('c', 1)
        ll.insert('a', 0)

        node = ll.find_by_data('c')
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")
        self.assertEqual(node.data, "c")
        self.assertEqual(node.prev.data, "b")
        self.assertIsNone(node.next)

    def test_find_by_data_not_found_on_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('b', 0)
        ll.insert('c', 1)
        ll.insert('a', 0)

        node = ll.find_by_data('x')
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")
        self.assertIsNone(node)

    def test_find_by_data_not_found_on_empty_list(self):
        ll = DoublyLinkedList()

        node = ll.find_by_data('x')
        self.assertEqual(len(ll), 0)
        self.assertEqual(str(ll), "[]")
        self.assertIsNone(node)

    def test_links_on_three_elem_list_001(self):
        ll = DoublyLinkedList()
        ll.insert('c', 0)
        ll.insert('a', 0)
        ll.insert('b', 1)

        first_node = ll.find_by_pos(0)
        second_node = ll.find_by_pos(1)
        third_node = ll.find_by_pos(2)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")
        self.assertIsNone(first_node.prev)
        self.assertEqual(first_node.data, 'a')
        self.assertEqual(first_node.next, second_node)
        self.assertEqual(second_node.prev, first_node)
        self.assertEqual(second_node.data, 'b')
        self.assertEqual(second_node.next, third_node)
        self.assertEqual(third_node.prev, second_node)
        self.assertEqual(third_node.data, 'c')
        self.assertIsNone(third_node.next)

    def test_links_on_three_elem_list_010(self):
        ll = DoublyLinkedList()
        ll.insert('b', 0)
        ll.insert('c', 1)
        ll.insert('a', 0)

        first_node = ll.find_by_pos(0)
        second_node = ll.find_by_pos(1)
        third_node = ll.find_by_pos(2)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")
        self.assertIsNone(first_node.prev)
        self.assertEqual(first_node.data, 'a')
        self.assertEqual(first_node.next, second_node)
        self.assertEqual(second_node.prev, first_node)
        self.assertEqual(second_node.data, 'b')
        self.assertEqual(second_node.next, third_node)
        self.assertEqual(third_node.prev, second_node)
        self.assertEqual(third_node.data, 'c')
        self.assertIsNone(third_node.next)

    def test_links_on_three_elem_list_000(self):
        ll = DoublyLinkedList()
        ll.insert('c', 0)
        ll.insert('b', 0)
        ll.insert('a', 0)

        first_node = ll.find_by_pos(0)
        second_node = ll.find_by_pos(1)
        third_node = ll.find_by_pos(2)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")
        self.assertIsNone(first_node.prev)
        self.assertEqual(first_node.data, 'a')
        self.assertEqual(first_node.next, second_node)
        self.assertEqual(second_node.prev, first_node)
        self.assertEqual(second_node.data, 'b')
        self.assertEqual(second_node.next, third_node)
        self.assertEqual(third_node.prev, second_node)
        self.assertEqual(third_node.data, 'c')
        self.assertIsNone(third_node.next)

    def test_links_on_three_elem_list_012(self):
        ll = DoublyLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)
        ll.insert('c', 2)

        first_node = ll.find_by_pos(0)
        second_node = ll.find_by_pos(1)
        third_node = ll.find_by_pos(2)

        self.assertFalse(ll.is_empty())
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")
        self.assertIsNone(first_node.prev)
        self.assertEqual(first_node.data, 'a')
        self.assertEqual(first_node.next, second_node)
        self.assertEqual(second_node.prev, first_node)
        self.assertEqual(second_node.data, 'b')
        self.assertEqual(second_node.next, third_node)
        self.assertEqual(third_node.prev, second_node)
        self.assertEqual(third_node.data, 'c')
        self.assertIsNone(third_node.next)

    def test_iter_three_elem_list(self):
        ll = DoublyLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)
        ll.insert('c', 2)

        res = [elem for elem in ll]
        self.assertEqual(res, ['a', 'b', 'c'])


if __name__ == "__main__":
    unittest.main()
