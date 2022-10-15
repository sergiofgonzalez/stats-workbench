import unittest
from cs09_heap_backed_linked_list import HeapBackedLinkedList

# to get the coverage reports install coverage package using `conda install coverage` (if not already there) and run:
# + `coverage run <name-of-the-file.py>
# + `coverage report` &mdash; text report
# + `coverage html` &mdash; html report


class TestHeapBackedLinkedList(unittest.TestCase):

    def test_initialize_list(self):
        ll = HeapBackedLinkedList()

        self.assertTrue(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 0)
        self.assertEqual(str(ll), "[]")

    def test_remove_from_empty_list_fails(self):
        ll = HeapBackedLinkedList()

        with self.assertRaises(Exception):
            ll.remove(0)

    def test_insert_first_elem_on_empty_list(self):
        ll = HeapBackedLinkedList()

        ll.insert('a', 0)

        self.assertFalse(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 1)
        self.assertEqual(str(ll), "[a]")

    def test_insert_second_elem_in_first_pos(self):
        ll = HeapBackedLinkedList()
        ll.insert('b', 0)

        ll.insert('a', 0)

        self.assertFalse(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 2)
        self.assertEqual(str(ll), "[a, b]")

    def test_insert_third_elem_in_first_pos(self):
        ll = HeapBackedLinkedList()
        ll.insert('c', 0)
        ll.insert('b', 0)

        ll.insert('a', 0)

        self.assertFalse(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")

    def test_insert_in_second_pos_in_list_with_2_elems(self):
        ll = HeapBackedLinkedList()
        ll.insert('c', 0)
        ll.insert('a', 0)

        ll.insert('b', 1)

        self.assertFalse(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")

    def test_insert_elem_in_third_pos_in_list_with_2_elems(self):
        ll = HeapBackedLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)

        ll.insert('c', 2)

        self.assertFalse(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")

    def test_insert_elems_in_last_pos_three_times(self):
        ll = HeapBackedLinkedList()

        ll.insert('a', len(ll))
        ll.insert('b', len(ll))
        ll.insert('c', len(ll))

        self.assertFalse(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")

    def test_insert_elem_in_first_pos_three_times(self):
        ll = HeapBackedLinkedList()

        ll.insert('c', 0)
        ll.insert('b', 0)
        ll.insert('a', 0)

        self.assertFalse(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), "[a, b, c]")

    def test_remove_first_elem_from_list_with_single_elem(self):
        ll = HeapBackedLinkedList()
        ll.insert('a', 0)

        ll.remove(0)

        self.assertTrue(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 0)
        self.assertEqual(str(ll), "[]")

    def test_remove_first_elem_from_list_with_two_elems(self):
        ll = HeapBackedLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)

        ll.remove(0)

        self.assertFalse(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 1)
        self.assertEqual(str(ll), "[b]")

    def test_remove_first_elem_from_list_with_three_elems(self):
        ll = HeapBackedLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)
        ll.insert('c', 2)

        ll.remove(0)

        self.assertFalse(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 2)
        self.assertEqual(str(ll), "[b, c]")

    def test_remove_second_elem_in_list_with_3_elems(self):
        ll = HeapBackedLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)
        ll.insert('c', 2)

        ll.remove(1)

        self.assertFalse(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 2)
        self.assertEqual(str(ll), "[a, c]")

    def test_remove_second_elem_in_list_with_2_elems(self):
        ll = HeapBackedLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)

        ll.remove(1)

        self.assertFalse(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 1)
        self.assertEqual(str(ll), "[a]")

    def test_remove_elem_in_last_position_until_empty(self):
        ll = HeapBackedLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)
        ll.insert('c', 2)

        ll.remove(len(ll) - 1)
        ll.remove(len(ll) - 1)

        # halfway through assertions
        self.assertFalse(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 1)
        self.assertEqual(str(ll), "[a]")

        # keep removing items
        ll.remove(len(ll) - 1)

        self.assertTrue(ll.is_empty())
        self.assertFalse(ll.is_full())
        self.assertEqual(len(ll), 0)
        self.assertEqual(str(ll), "[]")

    def test_insert_with_neg_pos_should_fail(self):
        ll = HeapBackedLinkedList()

        with self.assertRaises(Exception):
            ll.insert('will fail', -1)

    def test_insert_beyond_limits_empty_list_should_fail(self):
        ll = HeapBackedLinkedList()

        with self.assertRaises(Exception):
            ll.insert('a', 1)

    def test_insert_beyond_limits_non_empty_list_should_fail(self):
        ll = HeapBackedLinkedList()
        ll.insert('a', 0)

        with self.assertRaises(Exception):
            ll.insert('a', 2)

    def test_remove_neg_pos_should_fail(self):
        ll = HeapBackedLinkedList()

        with self.assertRaises(Exception):
            ll.remove(-1)

    def test_remove_beyond_limites_should_fail(self):
        ll = HeapBackedLinkedList()
        ll.insert('a', 0)

        with self.assertRaises(Exception):
            ll.remove(1)

    def test_object_is_iterable(self):
        ll = HeapBackedLinkedList()
        ll.insert('a', 0)
        ll.insert('b', 1)
        ll.insert('c', 2)

        equiv_list = [elem for elem in ll]
        self.assertEqual(len(equiv_list), len(ll))
        self.assertEqual(equiv_list[0], 'a')
        self.assertEqual(equiv_list[1], 'b')
        self.assertEqual(equiv_list[2], 'c')

    def test_long_running_shakedown(self):
        """This checks that the list's internal structures get updated correctly when you
        keep inserting and removing objects from the list.
        The previous tests got brand new lists for each of the tests.
        """

        ll = HeapBackedLinkedList()

        def test_list_initialization():
            self.assertTrue(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 0)
            self.assertEqual(str(ll), "[]")

        def test_remove_from_empty_list_fails():
            with self.assertRaises(Exception):
                ll.remove(0)

        def test_insert_first_elem_in_valid_pos():
            ll.insert('a', 0)

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 1)
            self.assertEqual(str(ll), "[a]")

        def test_remove_first_elem_from_a_list_with_single_element():
            ll.remove(0)

            self.assertTrue(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 0)
            self.assertEqual(str(ll), "[]")

        def test_insert_second_elem_in_first_pos():
            ll.insert('a', 0)

            ll.insert('b', 0)

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 2)
            self.assertEqual(str(ll), "[b, a]")

        def test_remove_first_elem_from_list_with_2_elems():
            ll.remove(0)

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 1)
            self.assertEqual(str(ll), "[a]")

        def test_insert_third_elem_in_first_pos():
            ll.insert('b', 0)

            ll.insert('c', 0)

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 3)
            self.assertEqual(str(ll), "[c, b, a]")

        def test_remove_first_elem_from_list_with_3_elems():
            ll.remove(0)

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 2)
            self.assertEqual(str(ll), "[b, a]")

        def test_insert_elem_in_second_pos_in_list_with_2_elems():
            ll.insert('X', 1)

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 3)
            self.assertEqual(str(ll), "[b, X, a]")

        def test_insert_elem_in_third_pos_in_list_with_2_elems():
            ll.remove(0)

            ll.insert('Z', 2)

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 3)
            self.assertEqual(str(ll), "[X, a, Z]")

        def test_insert_elems_in_last_pos_for_three_times():
            ll.remove(0)
            ll.remove(0)
            ll.remove(0)

            ll.insert('a', len(ll))
            ll.insert('b', len(ll))
            ll.insert('c', len(ll))

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 3)
            self.assertEqual(str(ll), "[a, b, c]")

        def test_insert_elems_in_first_pos_twice():
            ll.remove(0)
            ll.remove(0)

            ll.insert('Y', 0)
            ll.insert('X', 0)

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 3)
            self.assertEqual(str(ll), "[X, Y, c]")

        def test_insert_elems_in_mid_pos_twice():
            ll.remove(0)
            ll.remove(0)

            ll.insert('Y', 1)
            ll.insert('X', 1)

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 3)
            self.assertEqual(str(ll), "[c, X, Y]")

        def test_remove_elems_in_second_pos_in_list_with_3_elems():
            ll.remove(1)

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 2)
            self.assertEqual(str(ll), "[c, Y]")

        def test_remove_elem_in_second_pos_in_list_with_2_elems():
            ll.remove(1)

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 1)
            self.assertEqual(str(ll), "[c]")

        def test_remove_elem_in_last_pos_until_empty():
            ll.insert('x', 0)
            ll.insert('e', len(ll))

            # remove a couple of items and check
            ll.remove(len(ll) - 1)
            ll.remove(len(ll) - 1)

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 1)
            self.assertEqual(str(ll), "[x]")

            # remove the remaining elem and check
            ll.remove(len(ll) - 1)

            self.assertTrue(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 0)
            self.assertEqual(str(ll), "[]")

        def test_insert_beyond_limits_neg_pos():
            with self.assertRaises(Exception):
                ll.insert('X', -1)

        def test_insert_beyond_limits_post_len_empty_list():
            with self.assertRaises(Exception):
                ll.insert('X', 1)

        def test_insert_beyond_limits_on_non_empty_non_full_list_post_len():
            ll.insert('a', 0)
            ll.insert('b', 1)

            with self.assertRaises(Exception):
                ll.insert('X', len(ll) + 1)

        def test_insert_beyond_limits_on_full_list_post_len():
            ll.insert('c', 2)

            with self.assertRaises(Exception):
                ll.insert('X', len(ll) + 1)

        def test_remove_beyond_limits_neg_pos():
            with self.assertRaises(Exception):
                ll.remove(-1)

        def test_remove_beyond_limits_post_len():
            with self.assertRaises(Exception):
                ll.remove(len(ll))

        def test_insert_in_next_pos_in_non_full_list():
            ll.remove(0)

            ll.insert('a', len(ll))

            self.assertFalse(ll.is_empty())
            self.assertFalse(ll.is_full())
            self.assertEqual(len(ll), 3)
            self.assertEqual(str(ll), "[b, c, a]")

        test_list_initialization()
        test_remove_from_empty_list_fails()
        test_insert_first_elem_in_valid_pos()
        test_remove_first_elem_from_a_list_with_single_element()
        test_insert_second_elem_in_first_pos()
        test_remove_first_elem_from_list_with_2_elems()
        test_insert_third_elem_in_first_pos()
        test_remove_first_elem_from_list_with_3_elems()
        test_insert_elem_in_second_pos_in_list_with_2_elems()
        test_insert_elem_in_third_pos_in_list_with_2_elems()
        test_insert_elems_in_last_pos_for_three_times()
        test_insert_elems_in_first_pos_twice()
        test_insert_elems_in_mid_pos_twice()
        test_remove_elems_in_second_pos_in_list_with_3_elems()
        test_remove_elem_in_second_pos_in_list_with_2_elems()
        test_remove_elem_in_last_pos_until_empty()
        test_insert_beyond_limits_neg_pos()
        test_insert_beyond_limits_post_len_empty_list()
        test_insert_beyond_limits_on_non_empty_non_full_list_post_len()
        test_insert_beyond_limits_on_full_list_post_len()
        test_remove_beyond_limits_neg_pos()
        test_remove_beyond_limits_post_len()
        test_insert_in_next_pos_in_non_full_list()


if __name__ == "__main__":
    unittest.main()
