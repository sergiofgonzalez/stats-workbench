import unittest

from cs30_list_recursive_data_type import EMPTY, List

# to get the coverage reports install coverage package using `conda install coverage` (if not already there) and run:
# + `coverage run <name-of-the-file.py>
# + `coverage report` &mdash; text report
# + `coverage html` &mdash; html report


class TestList(unittest.TestCase):

    def test_calling_head_on_empty_list_raises(self):
        with self.assertRaises(Exception):
            EMPTY.head()

        with self.assertRaises(Exception):
            List.empty_list().head()

    def test_calling_tail_on_empty_list_raises(self):
        with self.assertRaises(Exception):
            EMPTY.tail()

        with self.assertRaises(Exception):
            List.empty_list.tail()

    def test_calling_tail_on_list_with_single_elem_return_empty_list(self):
        tail = List.list("one", EMPTY).tail()
        self.assertEqual(EMPTY, tail)

    def test_calling_head_on_list_with_single_elem_return_first_elem(self):
        head = List.list("one", EMPTY).head()
        self.assertEqual("one", head)

    def test_calling_tail_on_a_list_with_multiple_elems_returns_non_empty_list(self):
        tail = List.list("one", List.list("two", EMPTY)).tail()
        self.assertEqual(List.list("two", EMPTY), tail)

    def test_all_empty_lists_are_created_equal(self):
        emptytls = List.empty_list()
        emptyll = List.empty_list()

        self.assertEqual(emptyll, emptytls)
        self.assertEqual(EMPTY, emptyll)

    def test_list_are_recursive_structures(self):
        list_1 = List.list("one", List.list("two", List.list("three", EMPTY)))
        self.assertEqual(str(list_1), "(one, (two, (three, ())))")

    def test_search_on_empty_list_return_none(self):
        self.assertEqual(EMPTY.search("any"), None)

    def test_search_on_non_empty_list_not_found_return_none(self):
        ll = List.list('a', List.list('b', List.list('c', EMPTY)))

        self.assertEqual(ll.search('d'), None)

    def test_search_on_non_empty_list_found_in_head_return_elem(self):
        ll = List.list('a', List.list('b', List.list('c', EMPTY)))

        self.assertEqual(ll.search('a'), 'a')

    def test_search_on_non_empty_list_found_in_tail_return_elem(self):
        ll = List.list('a', List.list('b', List.list('c', EMPTY)))

        self.assertEqual(ll.search('b'), 'b')
        self.assertEqual(ll.search('c'), 'c')

    def test_create_from_elems_empty_list(self):
        ll = List.create_from_elems(*[])

        self.assertEqual(ll, EMPTY)

    def test_create_from_elems_list_with_single_elem(self):
        ll = List.create_from_elems('a')

        self.assertEqual(ll, List.list('a', EMPTY))

    def test_create_from_elems_list_with_two_elems(self):
        ll = List.create_from_elems('a', 'b')

        self.assertEqual(ll, List.list('a', List.list('b', EMPTY)))

    def test_create_from_elems_list_with_several_elems(self):
        ll = List.create_from_elems('a', 'e', 'i', 'o', 'u')

        self.assertEqual(ll, List.list('a', List.list('e', List.list('i', List.list('o', List.list('u', EMPTY))))))

    def test_generalized_list_work_ok(self):
        file_menu = List.create_from_elems('New', 'Open', 'Save', 'Exit')
        edit_menu = List.create_from_elems('Cut', 'Copy', 'Paste')
        help_menu = List.create_from_elems('Help', 'About')
        ll = List.create_from_elems(file_menu, edit_menu, help_menu)

        self.assertEqual(
            ll,
            List.list(
                List.list('New', List.list('Open', List.list('Save', List.list('Exit', EMPTY)))),
                List.list(
                    List.list('Cut', List.list('Copy', List.list('Paste', EMPTY))),
                    List.list(List.list('Help', List.list('About', EMPTY)), EMPTY)))
        )


if __name__ == "__main__":
    unittest.main()
