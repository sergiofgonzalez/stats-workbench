import unittest
from cs17_priority_queue import PriorityQueue

# to get the coverage reports install coverage package using `conda install coverage` (if not already there) and run:
# + `coverage run <name-of-the-file.py>
# + `coverage report` &mdash; text report
# + `coverage html` &mdash; html report


class TestPriorityQueue(unittest.TestCase):

    def test_priority_queue_can_be_created(self):
        pq = PriorityQueue()

        self.assertTrue(pq.is_empty())
        self.assertEqual(len(pq), 0)
        self.assertEqual(str(pq), "[]")

    def test_enqueue_on_empty_queue_default_sorting(self):
        pq = PriorityQueue()

        pq.insert('a')

        self.assertFalse(pq.is_empty())
        self.assertEqual(len(pq), 1)
        self.assertEqual(str(pq), "[a]")

    def test_enqueue_on_empty_queue_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))

        pq.insert('a')

        self.assertFalse(pq.is_empty())
        self.assertEqual(len(pq), 1)
        self.assertEqual(str(pq), "[a]")

    def test_enqueue_second_elem_after_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('a')

        pq.insert('b')

        self.assertFalse(pq.is_empty())
        self.assertEqual(len(pq), 2)
        self.assertEqual(str(pq), "[a, b]")

    def test_enqueue_second_elem_before_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')

        pq.insert('a')

        self.assertFalse(pq.is_empty())
        self.assertEqual(len(pq), 2)
        self.assertEqual(str(pq), "[a, b]")

    def test_enqueue_three_elems_before_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')

        pq.insert('a')

        self.assertFalse(pq.is_empty())
        self.assertEqual(len(pq), 3)
        self.assertEqual(str(pq), "[a, b, e]")

    def test_enqueue_three_elems_mid_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')

        pq.insert('c')

        self.assertFalse(pq.is_empty())
        self.assertEqual(len(pq), 3)
        self.assertEqual(str(pq), "[b, c, e]")

    def test_enqueue_three_elems_last_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')

        pq.insert('h')

        self.assertFalse(pq.is_empty())
        self.assertEqual(len(pq), 3)
        self.assertEqual(str(pq), "[b, e, h]")

    def test_in_empty_queue_default_sorting(self):
        pq = PriorityQueue()

        self.assertFalse('a' in pq)

    def test_in_one_elem_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('a')

        self.assertTrue('a' in pq)

    def test_in_one_elem_not_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('a')

        self.assertFalse('b' in pq)

    def test_in_three_elems_before_not_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertFalse('a' in pq)

    def test_in_three_elems_first_elem_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertTrue('b' in pq)

    def test_in_three_elems_after_first_elem_not_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertFalse('c' in pq)

    def test_in_three_elems_second_elem_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertTrue('e' in pq)

    def test_in_three_elems_after_second_elem_not_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertFalse('g' in pq)

    def test_in_three_elems_third_elem_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertTrue('h' in pq)

    def test_in_three_elems_after_third_elem_not_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertFalse('z' in pq)

    def test_remove_empty_queue_default_sorting(self):
        pq = PriorityQueue()

        is_removed = pq.remove('a')

        self.assertFalse(is_removed)
        self.assertEqual(str(pq), "[]")

    def test_remove_one_elem_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('a')

        is_removed = pq.remove('a')

        self.assertTrue(is_removed)
        self.assertEqual(str(pq), "[]")

    def test_remove_one_elem_not_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('a')

        is_removed = pq.remove('b')
        self.assertFalse(is_removed)
        self.assertEqual(str(pq), "[a]")

    def test_remove_three_elems_before_not_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('a')

        self.assertFalse(is_removed)
        self.assertEqual(str(pq), "[b, e, h]")

    def test_remove_three_elems_first_elem_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('b')

        self.assertTrue(is_removed)
        self.assertEqual(str(pq), "[e, h]")

    def test_remove_three_elems_after_first_elem_not_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('c')

        self.assertFalse(is_removed)
        self.assertEqual(str(pq), "[b, e, h]")

    def test_remove_three_elems_second_elem_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('e')

        self.assertTrue(is_removed)
        self.assertEqual(str(pq), "[b, h]")

    def test_remove_three_elems_after_second_elem_not_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('g')

        self.assertFalse(is_removed)
        self.assertEqual(str(pq), "[b, e, h]")

    def test_remove_three_elems_third_elem_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('h')

        self.assertTrue(is_removed)
        self.assertEqual(str(pq), "[b, e]")

    def test_remove_three_elems_after_third_elem_not_found_default_sorting(self):
        pq = PriorityQueue()
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('z')

        self.assertFalse(is_removed)
        self.assertEqual(str(pq), "[b, e, h]")

    def test_iteration_empty_queue_default_sorting(self):
        pq = PriorityQueue()

        elems = [elem for elem in pq]

        self.assertEqual(elems, [])

    def test_iteration_single_elem_queue_default_sorting(self):
        q = PriorityQueue()
        q.insert('a')

        elems = [elem for elem in q]

        self.assertEqual(elems, ['a'])

    def test_iteration_three_elems_queue_default_sorting(self):
        q = PriorityQueue()
        q.insert('a')
        q.insert('b')
        q.insert('c')

        elems = [elem for elem in q]

        self.assertEqual(elems, ['a', 'b', 'c'])

    def test_priority_queue_can_be_created_non_default_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))

        self.assertTrue(pq.is_empty())
        self.assertEqual(len(pq), 0)
        self.assertEqual(str(pq), "[]")

    def test_enqueue_second_elem_after_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('a')

        pq.insert('b')

        self.assertFalse(pq.is_empty())
        self.assertEqual(len(pq), 2)
        self.assertEqual(str(pq), "[b, a]")

    def test_enqueue_second_elem_before_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')

        pq.insert('a')

        self.assertFalse(pq.is_empty())
        self.assertEqual(len(pq), 2)
        self.assertEqual(str(pq), "[b, a]")

    def test_enqueue_three_elems_before_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')

        pq.insert('a')

        self.assertFalse(pq.is_empty())
        self.assertEqual(len(pq), 3)
        self.assertEqual(str(pq), "[e, b, a]")

    def test_enqueue_three_elems_mid_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')

        pq.insert('c')

        self.assertFalse(pq.is_empty())
        self.assertEqual(len(pq), 3)
        self.assertEqual(str(pq), "[e, c, b]")

    def test_enqueue_three_elems_last_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')

        pq.insert('h')

        self.assertFalse(pq.is_empty())
        self.assertEqual(len(pq), 3)
        self.assertEqual(str(pq), "[h, e, b]")

    def test_in_empty_queue_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))

        self.assertFalse('a' in pq)

    def test_in_one_elem_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('a')

        self.assertTrue('a' in pq)

    def test_in_one_elem_not_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('a')

        self.assertFalse('b' in pq)

    def test_in_three_elems_before_not_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertFalse('a' in pq)

    def test_in_three_elems_first_elem_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertTrue('b' in pq)

    def test_in_three_elems_after_first_elem_not_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertFalse('c' in pq)

    def test_in_three_elems_second_elem_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertTrue('e' in pq)

    def test_in_three_elems_after_second_elem_not_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertFalse('g' in pq)

    def test_in_three_elems_third_elem_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertTrue('h' in pq)

    def test_in_three_elems_after_third_elem_not_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        self.assertFalse('z' in pq)

    def test_remove_empty_queue_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))

        is_removed = pq.remove('a')

        self.assertFalse(is_removed)
        self.assertEqual(str(pq), "[]")

    def test_remove_one_elem_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('a')

        is_removed = pq.remove('a')

        self.assertTrue(is_removed)
        self.assertEqual(str(pq), "[]")

    def test_remove_one_elem_not_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('a')

        is_removed = pq.remove('b')
        self.assertFalse(is_removed)
        self.assertEqual(str(pq), "[a]")

    def test_remove_three_elems_before_not_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('a')

        self.assertFalse(is_removed)
        self.assertEqual(str(pq), "[h, e, b]")

    def test_remove_three_elems_first_elem_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('b')

        self.assertTrue(is_removed)
        self.assertEqual(str(pq), "[h, e]")

    def test_remove_three_elems_after_first_elem_not_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('c')

        self.assertFalse(is_removed)
        self.assertEqual(str(pq), "[h, e, b]")

    def test_remove_three_elems_second_elem_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('e')

        self.assertTrue(is_removed)
        self.assertEqual(str(pq), "[h, b]")

    def test_remove_three_elems_after_second_elem_not_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('g')

        self.assertFalse(is_removed)
        self.assertEqual(str(pq), "[h, e, b]")

    def test_remove_three_elems_third_elem_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('h')

        self.assertTrue(is_removed)
        self.assertEqual(str(pq), "[e, b]")

    def test_remove_three_elems_after_third_elem_not_found_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))
        pq.insert('b')
        pq.insert('e')
        pq.insert('h')

        is_removed = pq.remove('z')

        self.assertFalse(is_removed)
        self.assertEqual(str(pq), "[h, e, b]")

    def test_iteration_empty_queue_custom_sorting(self):
        pq = PriorityQueue(lambda x, y: ord(y) - ord(x))

        elems = [elem for elem in pq]

        self.assertEqual(elems, [])

    def test_iteration_single_elem_queue_custom_sorting(self):
        q = PriorityQueue(lambda x, y: ord(y) - ord(x))
        q.insert('a')

        elems = [elem for elem in q]

        self.assertEqual(elems, ['a'])

    def test_iteration_three_elems_queue_custom_sorting(self):
        q = PriorityQueue(lambda x, y: ord(y) - ord(x))
        q.insert('a')
        q.insert('b')
        q.insert('c')

        elems = [elem for elem in q]

        self.assertEqual(elems, ['c', 'b', 'a'])


if __name__ == "__main__":
    unittest.main()
