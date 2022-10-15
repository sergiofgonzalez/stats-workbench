class Stack:
    def __init__(self):
        self.items = []

    def push(self, elem):
        self.items.append(elem)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __repr__(self):
        str = ""
        for i in range(0, len(self.items)):
            str += f"\n{len(self.items) - 1 - i}: {self.items[i]}"
        return str


if __name__ == "__main__":
    print("Testing the stack")
    num_stack = Stack()

    # pushing a couple of items
    num_stack.push(1)
    print(num_stack.items)
    num_stack.push(2)
    print(num_stack.items)

    # using __repr__
    print(num_stack)
    print()

    # peeking the head (should get last pushed elem)
    head = num_stack.peek()
    print(head)

    # popping the top of the stack (should get last pushed elem)
    head = num_stack.pop()
    print(head)
    print(num_stack.items)

    # popping another elem
    head = num_stack.pop()
    print(head)
    print(num_stack.items)

    # popping from empty list (should raise exception)
    try:
        head = num_stack.pop()
    except Exception as ex:
        print(f"got '{ex}' error when popping from empty list")
