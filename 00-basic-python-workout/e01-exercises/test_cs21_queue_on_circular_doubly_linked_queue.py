import unittest
from cs21_queue_on_circular_doubly_linked_list import Queue
# to get the coverage reports install coverage package using `conda install coverage` (if not already there) and run:
# + `coverage run <name-of-the-file.py>
# + `coverage report` &mdash; text report
# + `coverage html` &mdash; html report


class TestQueueOnCircularDoublyLinkedList(unittest.TestCase):

    def test_initialize_queue(self):
        q = Queue()

        self.assertTrue(q.is_empty())
        self.assertEqual(len(q), 0)
        self.assertEqual(str(q), "[]")

    def test_remove_from_empty_queue_fails(self):
        q = Queue()

        with self.assertRaises(Exception):
            q.remove()

    def test_dequeue_from_empty_queue_fails(self):
        q = Queue()

        with self.assertRaises(Exception):
            q.dequeue()

    def test_insert_single_elem(self):
        q = Queue()

        q.insert('a')

        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 1)
        self.assertEqual(str(q), "[a]")

    def test_enqueue_single_elem(self):
        q = Queue()

        q.enqueue('a')

        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 1)
        self.assertEqual(str(q), "[a]")

    def test_remove_single_elem_queue(self):
        q = Queue()
        q.enqueue('a')

        head = q.remove()

        self.assertTrue(q.is_empty())
        self.assertEqual(len(q), 0)
        self.assertEqual(str(q), "[]")
        self.assertEqual(head, 'a')

    def test_dequeue_single_elem_queue(self):
        q = Queue()
        q.enqueue('a')

        head = q.dequeue()

        self.assertTrue(q.is_empty())
        self.assertEqual(len(q), 0)
        self.assertEqual(str(q), "[]")
        self.assertEqual(head, 'a')

    def test_insert_two_elem(self):
        q = Queue()

        q.enqueue('a')
        q.enqueue('b')

        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 2)
        self.assertEqual(str(q), "[a, b]")

    def test_enqueue_two_elem(self):
        q = Queue()

        q.enqueue('a')
        q.enqueue('b')

        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 2)
        self.assertEqual(str(q), "[a, b]")

    def test_remove_two_elem(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')

        head = q.remove()

        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 1)
        self.assertEqual(str(q), "[b]")
        self.assertEqual(head, 'a')

    def test_dequeue_two_elem(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')

        head = q.remove()

        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 1)
        self.assertEqual(str(q), "[b]")
        self.assertEqual(head, 'a')

    def test_remove_twice(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')

        head_1 = q.remove()
        head_2 = q.remove()

        self.assertTrue(q.is_empty())
        self.assertEqual(len(q), 0)
        self.assertEqual(str(q), "[]")
        self.assertEqual(head_1, 'a')
        self.assertEqual(head_2, 'b')

    def test_dequeue_twice(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')

        head_1 = q.dequeue()
        head_2 = q.dequeue()

        self.assertTrue(q.is_empty())
        self.assertEqual(len(q), 0)
        self.assertEqual(str(q), "[]")
        self.assertEqual(head_1, 'a')
        self.assertEqual(head_2, 'b')


if __name__ == "__main__":
    unittest.main()
