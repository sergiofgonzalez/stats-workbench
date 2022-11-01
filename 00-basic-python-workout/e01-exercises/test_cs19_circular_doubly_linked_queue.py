import unittest
from cs19_circular_doubly_linked_list import CircularDoublyLinkedList
# to get the coverage reports install coverage package using `conda install coverage` (if not already there) and run:
# + `coverage run <name-of-the-file.py>
# + `coverage report` &mdash; text report
# + `coverage html` &mdash; html report


class TestCircularDoublyLinkedList(unittest.TestCase):

    def test_initialize_list(self):
        cll = CircularDoublyLinkedList()

        self.assertTrue(cll.is_empty())
        self.assertEqual(len(cll), 0)
        self.assertEqual(str(cll), "[]")

    def test_remove_from_empty_list_fails(self):
        cll = CircularDoublyLinkedList()

        with self.assertRaises(Exception):
            cll.remove(0)

    def test_insert_first_elem_on_empty_list(self):
        cll = CircularDoublyLinkedList()

        cll.insert('a', 0)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 1)
        self.assertEqual(str(cll), "[a]")

    def test_insert_two_elems_in_first_pos(self):
        cll = CircularDoublyLinkedList()

        cll.insert('b', 0)
        cll.insert('a', 0)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[a, b]")

    def test_insert_three_elems_in_first_pos(self):
        cll = CircularDoublyLinkedList()

        cll.insert('c', 0)
        cll.insert('b', 0)
        cll.insert('a', 0)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")

    def test_insert_two_elems_in_succession(self):
        cll = CircularDoublyLinkedList()

        cll.insert('a', 0)
        cll.insert('b', 1)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[a, b]")

    def test_insert_three_elems_in_succession(self):
        cll = CircularDoublyLinkedList()

        cll.insert('a', 0)
        cll.insert('b', 1)
        cll.insert('c', 2)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")

    def test_insert_three_elems_not_in_succession(self):
        cll = CircularDoublyLinkedList()

        cll.insert('a', 0)
        cll.insert('c', 1)
        cll.insert('b', 1)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")

    def test_insert_5_elems_in_succession(self):
        cll = CircularDoublyLinkedList()

        cll.insert('a', len(cll))
        cll.insert('b', len(cll))
        cll.insert('c', len(cll))
        cll.insert('d', len(cll))
        cll.insert('e', len(cll))

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 5)
        self.assertEqual(str(cll), "[a, b, c, d, e]")

    def test_insert_5_elems_not_in_succession(self):
        cll = CircularDoublyLinkedList()

        cll.insert('a', 0)
        cll.insert('e', 1)
        cll.insert('c', 1)
        cll.insert('b', 1)
        cll.insert('d', 3)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 5)
        self.assertEqual(str(cll), "[a, b, c, d, e]")

    def test_remove_elem_in_first_pos(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)

        cll.remove(0)

        self.assertTrue(cll.is_empty())
        self.assertEqual(len(cll), 0)
        self.assertEqual(str(cll), "[]")

    def test_remove_elems_in_second_pos_from_list_with_two_elems(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)

        cll.remove(1)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 1)
        self.assertEqual(str(cll), "[a]")

    def test_remove_elems_in_last_pos(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)
        cll.insert('c', 2)
        cll.insert('d', 3)
        cll.insert('e', 4)

        cll.remove(len(cll) - 1)
        self.assertEqual(len(cll), 4)
        self.assertEqual(str(cll), "[a, b, c, d]")

        cll.remove(len(cll) - 1)
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")

        cll.remove(len(cll) - 1)
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[a, b]")

        cll.remove(len(cll) - 1)
        self.assertEqual(len(cll), 1)
        self.assertEqual(str(cll), "[a]")

        cll.remove(len(cll) - 1)
        self.assertTrue(cll.is_empty())
        self.assertEqual(len(cll), 0)
        self.assertEqual(str(cll), "[]")

    def test_remove_elems_in_first_pos_from_list_with_two_elems(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)

        cll.remove(0)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 1)
        self.assertEqual(str(cll), "[b]")

    def test_remove_elems(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)
        cll.insert('c', 2)
        cll.insert('d', 3)
        cll.insert('e', 4)

        cll.remove(3)
        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 4)
        self.assertEqual(str(cll), "[a, b, c, e]")

        cll.remove(2)
        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, e]")

        cll.remove(1)
        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[a, e]")

        cll.remove(1)
        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 1)
        self.assertEqual(str(cll), "[a]")

        cll.remove(0)
        self.assertTrue(cll.is_empty())
        self.assertEqual(len(cll), 0)
        self.assertEqual(str(cll), "[]")

    def test_iter_is_circular(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)
        cll.insert('c', 2)
        cll.insert('d', 3)
        cll.insert('e', 4)

        tuples = list(zip(range(len(cll) + 2), cll))
        self.assertEqual(tuples[0], (0, 'a'))
        self.assertEqual(tuples[1], (1, 'b'))
        self.assertEqual(tuples[2], (2, 'c'))
        self.assertEqual(tuples[3], (3, 'd'))
        self.assertEqual(tuples[4], (4, 'e'))
        self.assertEqual(tuples[5], (5, 'a'))
        self.assertEqual(tuples[6], (6, 'b'))

    def test_iter_over_empty_circular_list(self):
        cll = CircularDoublyLinkedList()
        result = [elem for elem in cll]
        self.assertEqual(result, [])

    def test_node_to_string(self):
        node = CircularDoublyLinkedList.Node('data', 'prev', 'next')
        self.assertEqual(str(node), "(data=data, prev=prev, next=next)")

    def test_list_can_be_created(self):
        cll = CircularDoublyLinkedList()

        self.assertTrue(cll.is_empty())
        self.assertEqual(len(cll), 0)
        self.assertEqual(str(cll), "[]")

    def test_insert_first_elem_below_zero(self):
        cll = CircularDoublyLinkedList()

        with self.assertRaises(Exception):
            cll.insert('a', -1)

    def test_insert_first_elem_beyond_zero(self):
        cll = CircularDoublyLinkedList()

        with self.assertRaises(Exception):
            cll.insert('a', 1)

    def test_insert_first_elem(self):
        cll = CircularDoublyLinkedList()

        cll.insert('a', 0)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 1)
        self.assertEqual(str(cll), "[a]")

    def test_insert_second_elem_beyond_len(self):
        cll = CircularDoublyLinkedList()

        cll.insert('a', 0)

        with self.assertRaises(Exception):
            cll.insert('b', len(cll) + 1)

    def test_insert_as_first_in_two_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('b', 0)

        cll.insert('a', 0)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[a, b]")

    def test_insert_as_second_in_two_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)

        cll.insert('b', 1)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[a, b]")

    def test_insert_before_first_in_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('b', 0)
        cll.insert('e', 1)
        cll.insert('h', 2)

        cll.insert('a', 0)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 4)
        self.assertEqual(str(cll), "[a, b, e, h]")

    def test_insert_before_second_in_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('b', 0)
        cll.insert('e', 1)
        cll.insert('h', 2)

        cll.insert('c', 1)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 4)
        self.assertEqual(str(cll), "[b, c, e, h]")

    def test_insert_before_third_in_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('b', 0)
        cll.insert('e', 1)
        cll.insert('h', 2)

        cll.insert('f', 2)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 4)
        self.assertEqual(str(cll), "[b, e, f, h]")

    def test_insert_after_third_in_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('b', 0)
        cll.insert('e', 1)
        cll.insert('h', 2)

        cll.insert('k', 3)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 4)
        self.assertEqual(str(cll), "[b, e, h, k]")

    def test_remove_below_bounds_fails(self):
        cll = CircularDoublyLinkedList()

        with self.assertRaises(Exception):
            cll.remove(-1)

    def test_remove_on_empty_list_fails(self):
        cll = CircularDoublyLinkedList()

        with self.assertRaises(Exception):
            cll.remove(0)

    def test_remove_beyond_bound_fails(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)

        with self.assertRaises(Exception):
            cll.remove(1)

    def test_remove_elem_from_list_one_elem(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)

        cll.remove(0)

        self.assertTrue(cll.is_empty())
        self.assertEqual(len(cll), 0)
        self.assertEqual(str(cll), "[]")

    def test_remove_first_elem_from_two_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)

        cll.remove(0)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 1)
        self.assertEqual(str(cll), "[b]")

    def test_remove_second_elem_from_two_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)

        cll.remove(1)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 1)
        self.assertEqual(str(cll), "[a]")

    def test_remove_first_elem_from_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)
        cll.insert('c', 2)

        cll.remove(0)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[b, c]")

    def test_remove_second_elem_from_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)
        cll.insert('c', 2)

        cll.remove(1)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[a, c]")

    def test_remove_third_elem_from_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)
        cll.insert('c', 2)

        cll.remove(2)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[a, b]")

    def test_find_by_pos_below_bounds_neg(self):
        cll = CircularDoublyLinkedList()

        with self.assertRaises(Exception):
            cll.find_by_pos(-1)

    def test_find_by_pos_beyond_bounds_empty_list(self):
        cll = CircularDoublyLinkedList()

        with self.assertRaises(Exception):
            cll.find_by_pos(0)

    def test_find_by_pos_beyond_bounds_non_empty(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)

        with self.assertRaises(Exception):
            cll.find_by_pos(1)

    def test_find_by_pos_first_elem_on_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('c', 0)
        cll.insert('b', 0)
        cll.insert('a', 0)

        node = cll.find_by_pos(0)

        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")
        self.assertEqual(node.data, "a")
        self.assertEqual(node.prev.data, "c")
        self.assertEqual(node.next.data, "b")
        self.assertEqual(node.next.prev.data, "a")
        self.assertEqual(node.prev, cll.tail)

    def test_find_by_pos_second_elem_on_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('c', 0)
        cll.insert('b', 0)
        cll.insert('a', 0)

        node = cll.find_by_pos(1)

        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")
        self.assertEqual(node.data, "b")
        self.assertEqual(node.prev.data, "a")
        self.assertEqual(node.next.data, "c")
        self.assertEqual(node.next.prev.data, "b")

    def test_find_by_pos_third_elem_on_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('c', 0)
        cll.insert('b', 0)
        cll.insert('a', 0)

        node = cll.find_by_pos(2)

        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")
        self.assertEqual(node.data, "c")
        self.assertEqual(node.prev.data, "b")
        self.assertEqual(node.next.data, "a")
        self.assertEqual(node.prev.next.data, "c")

    def test_find_by_data_find_first_on_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('b', 0)
        cll.insert('c', 1)
        cll.insert('a', 0)

        node = cll.find_by_data('a')
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")
        self.assertEqual(node.data, "a")
        self.assertEqual(node.prev.data, "c")
        self.assertEqual(node.next.data, 'b')
        self.assertEqual(node.next.prev.data, 'a')

    def test_find_by_data_find_second_on_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('b', 0)
        cll.insert('c', 1)
        cll.insert('a', 0)

        node = cll.find_by_data('b')
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")
        self.assertEqual(node.data, "b")
        self.assertEqual(node.prev.data, "a")
        self.assertEqual(node.next.data, "c")

    def test_find_by_data_find_third_on_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('b', 0)
        cll.insert('c', 1)
        cll.insert('a', 0)

        node = cll.find_by_data('c')
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")
        self.assertEqual(node.data, "c")
        self.assertEqual(node.prev.data, "b")
        self.assertEqual(node.next.data, "a")

    def test_find_by_data_not_found_on_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('b', 0)
        cll.insert('c', 1)
        cll.insert('a', 0)

        node = cll.find_by_data('x')
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")
        self.assertIsNone(node)

    def test_find_by_data_not_found_on_empty_list(self):
        cll = CircularDoublyLinkedList()

        node = cll.find_by_data('x')
        self.assertEqual(len(cll), 0)
        self.assertEqual(str(cll), "[]")
        self.assertIsNone(node)

    def test_links_on_three_elem_list_001(self):
        cll = CircularDoublyLinkedList()
        cll.insert('c', 0)
        cll.insert('a', 0)
        cll.insert('b', 1)

        first_node = cll.find_by_pos(0)
        second_node = cll.find_by_pos(1)
        third_node = cll.find_by_pos(2)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")
        self.assertEqual(first_node.prev, third_node)
        self.assertEqual(first_node.data, 'a')
        self.assertEqual(first_node.next, second_node)
        self.assertEqual(second_node.prev, first_node)
        self.assertEqual(second_node.data, 'b')
        self.assertEqual(second_node.next, third_node)
        self.assertEqual(third_node.prev, second_node)
        self.assertEqual(third_node.data, 'c')
        self.assertEqual(third_node.next, first_node)

    def test_links_on_three_elem_list_010(self):
        cll = CircularDoublyLinkedList()
        cll.insert('b', 0)
        cll.insert('c', 1)
        cll.insert('a', 0)

        first_node = cll.find_by_pos(0)
        second_node = cll.find_by_pos(1)
        third_node = cll.find_by_pos(2)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")
        self.assertEqual(first_node.prev, third_node)
        self.assertEqual(first_node.data, 'a')
        self.assertEqual(first_node.next, second_node)
        self.assertEqual(second_node.prev, first_node)
        self.assertEqual(second_node.data, 'b')
        self.assertEqual(second_node.next, third_node)
        self.assertEqual(third_node.prev, second_node)
        self.assertEqual(third_node.data, 'c')
        self.assertEqual(third_node.next, first_node)

    def test_links_on_three_elem_list_000(self):
        cll = CircularDoublyLinkedList()
        cll.insert('c', 0)
        cll.insert('b', 0)
        cll.insert('a', 0)

        first_node = cll.find_by_pos(0)
        second_node = cll.find_by_pos(1)
        third_node = cll.find_by_pos(2)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")
        self.assertEqual(first_node.prev, third_node)
        self.assertEqual(first_node.data, 'a')
        self.assertEqual(first_node.next, second_node)
        self.assertEqual(second_node.prev, first_node)
        self.assertEqual(second_node.data, 'b')
        self.assertEqual(second_node.next, third_node)
        self.assertEqual(third_node.prev, second_node)
        self.assertEqual(third_node.data, 'c')
        self.assertEqual(third_node.next, first_node)

    def test_links_on_two_elem_list_01(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)

        first_node = cll.find_by_pos(0)
        second_node = cll.find_by_pos(1)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[a, b]")
        self.assertEqual(first_node.data, "a")
        self.assertEqual(second_node.data, "b")
        self.assertEqual(cll.tail, second_node)
        self.assertEqual(first_node.next, second_node)
        self.assertEqual(first_node.prev, second_node)
        self.assertEqual(second_node.next, first_node)
        self.assertEqual(second_node.prev, first_node)

    def test_links_on_two_elem_list_00(self):
        cll = CircularDoublyLinkedList()
        cll.insert('b', 0)
        cll.insert('a', 0)

        first_node = cll.find_by_pos(0)
        second_node = cll.find_by_pos(1)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[a, b]")
        self.assertEqual(first_node.data, "a")
        self.assertEqual(second_node.data, "b")
        self.assertEqual(cll.tail, second_node)
        self.assertEqual(first_node.next, second_node)
        self.assertEqual(first_node.prev, second_node)
        self.assertEqual(second_node.next, first_node)
        self.assertEqual(second_node.prev, first_node)

    def test_links_on_three_elem_list_012(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)
        cll.insert('c', 2)

        first_node = cll.find_by_pos(0)
        second_node = cll.find_by_pos(1)
        third_node = cll.find_by_pos(2)

        self.assertFalse(cll.is_empty())
        self.assertEqual(len(cll), 3)
        self.assertEqual(str(cll), "[a, b, c]")
        self.assertEqual(first_node.data, 'a')
        self.assertEqual(second_node.data, 'b')
        self.assertEqual(third_node.data, 'c')
        self.assertEqual(first_node.prev, third_node)
        self.assertEqual(first_node.next, second_node)
        self.assertEqual(second_node.prev, first_node)
        self.assertEqual(second_node.next, third_node)
        self.assertEqual(third_node.prev, second_node)
        self.assertEqual(third_node.next, first_node)

    def test_iter_three_elem_list(self):
        cll = CircularDoublyLinkedList()
        cll.insert('a', 0)
        cll.insert('b', 1)
        cll.insert('c', 2)

        res = [elem for elem in cll]
        self.assertEqual(res, ['a', 'b', 'c'])


if __name__ == "__main__":
    unittest.main()
