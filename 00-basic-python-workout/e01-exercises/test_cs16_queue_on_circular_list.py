import unittest
from cs16_queue_on_circular_list import Queue

# to get the coverage reports install coverage package using `conda install coverage` (if not already there) and run:
# + `coverage run <name-of-the-file.py>
# + `coverage report` &mdash; text report
# + `coverage html` &mdash; html report


class TestQueue(unittest.TestCase):

    def test_enqueue_first_elem(self):
        q = Queue()

        q.enqueue('a')
        head = q.head()

        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 1)
        self.assertEqual(str(q), "[a]")
        self.assertEqual(head, 'a')

    def test_enqueue_several_elems(self):
        q = Queue()

        q.enqueue('a')
        q.enqueue('b')
        head = q.head()

        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 2)
        self.assertEqual(str(q), "[a, b]")
        self.assertEqual(head, 'a')

    def test_dequeue_empty_q_should_fail(self):
        q = Queue()

        with self.assertRaises(Exception):
            q.remove()

    def test_dequeue_one_elem(self):
        q = Queue()

        q.enqueue('a')
        head = q.dequeue()

        self.assertTrue(q.is_empty())
        self.assertEqual(len(q), 0)
        self.assertEqual(str(q), "[]")
        self.assertEqual(head, 'a')

    def test_dequeue_two_elems(self):
        q = Queue()

        q.enqueue('a')
        q.enqueue('b')
        head = q.dequeue()

        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 1)
        self.assertEqual(str(q), "[b]")
        self.assertEqual(head, 'a')

    def test_head_on_empty_queue_fails(self):
        q = Queue()

        with self.assertRaises(Exception):
            q.head()

    def test_head_on_queue_with_one_elem(self):
        q = Queue()
        q.enqueue('a')

        head = q.head()

        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 1)
        self.assertEqual(str(q), "[a]")
        self.assertEqual(head, 'a')

    def test_head_on_queue_with_several_elems(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')

        head = q.head()

        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 2)
        self.assertEqual(str(q), "[a, b]")
        self.assertEqual(head, 'a')

    def test_iteration_empty_queue(self):
        q = Queue()

        elems = [elem for elem in q]

        self.assertEqual(elems, [])

    def test_iteration_queue_single_elem(self):
        q = Queue()
        q.enqueue('a')

        elems = [elem for elem in q]

        self.assertEqual(elems, ['a'])

    def test_iteration_queue_several_elems(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')

        elems = [elem for elem in q]

        self.assertEqual(elems, ['a', 'b', 'c'])

if __name__ == "__main__":
    unittest.main()
