# simplistic approach at recursive data structures: the Tree

class Tree:
    def __init__(self, left, value, right) -> None:
        self.left = left
        self.value = value
        self.right = right

    def __repr__(self):
        left_str = "^" if self.left is None else str(self.left)
        right_str = "^" if self.right is None else str(self.right)
        return f"({left_str}-{self.value}-{right_str})"


if __name__ == "__main__":
    print("Please run test_cs27_recursive_data_structures_tree.py")
