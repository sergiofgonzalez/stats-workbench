import unittest
from cs27_recursive_data_structures_tree import Tree
# to get the coverage reports install coverage package using `conda install coverage` (if not already there) and run:
# + `coverage run <name-of-the-file.py>
# + `coverage report` &mdash; text report
# + `coverage html` &mdash; html report


class TestTree(unittest.TestCase):

    def test_tree_with_root_only(self):
        root = Tree(None, 'a', None)

        self.assertEqual(str(root), "(^-a-^)")

    def test_simple_tree_with_leaves_1(self):
        """
                      1
                 ╔════╩════╗
                 2         3
        """

        root = Tree(
            Tree(None, 2, None),
            1,
            Tree(None, 3, None)
        )

        self.assertEqual(str(root), "((^-2-^)-1-(^-3-^))")

    def test_simple_tree_with_leaves_2(self):
        """
                      1
                 ╔════╝
                 2
        """

        root = Tree(
            Tree(None, 2, None),
            1,
            None
        )

        self.assertEqual(str(root), "((^-2-^)-1-^)")

    def test_complex_tree_with_leaves(self):
        """
                      1
                 ╔════╩════╗
                 2         6
              ╔══╩══╗   ╔══╩══╗
              3     4   7     8
                 ╔══╩══╗
                 5    None
        """

        root = Tree(
            Tree(
                Tree(None, 3, None), 2, Tree(Tree(None, 5, None), 4, None)),
            1,
            Tree(
                Tree(None, 7, None), 6, Tree(None, 8, None))
        )

        self.assertEqual(str(root), "(((^-3-^)-2-((^-5-^)-4-^))-1-((^-7-^)-6-(^-8-^)))")


if __name__ == "__main__":
    unittest.main()
