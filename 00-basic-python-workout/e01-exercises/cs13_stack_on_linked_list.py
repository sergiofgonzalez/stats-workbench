from cs12_better_generalized_linked_list import LinkedList, ArrayBackedLinkedList, HeapBackedLinkedList


class Stack(LinkedList):

    def push(self, elem):
        self.insert(elem, 0)

    def pop(self):
        if self.is_empty():
            raise "Cannot pop on empty Stack"
        head_elem = (self.node_from_ref(self._head_ref)).data
        self.remove(0)
        return head_elem

    def peek(self):
        if self.is_empty():
            raise "Cannot peek on empty Stack"
        head_elem = (self.node_from_ref(self._head_ref)).data
        return head_elem

    def __repr__(self):
        if self.is_empty():
            return "-- empty stack --"
        elems_str = [f"{i}: {elem}" for (elem, i) in zip(self, range(len(self)))]
        return "\n".join(reversed(elems_str))


class ArrayBackedStack(Stack, ArrayBackedLinkedList):
    ...


class HeapBackedStack(Stack, HeapBackedLinkedList):
    ...


if __name__ == "__main__":
    print("== ArrayBackedStack")
    stack = ArrayBackedStack(10)
    print(stack)

    # pushing first elem
    print()
    stack.push("first")
    print(stack)

    # pushing second elem
    print()
    stack.push("second")
    print(stack)

    # pushing third elem
    print()
    stack.push("third")
    print(stack)

    # peeking
    print()
    top_of_stack = stack.peek()
    print(f"top: {top_of_stack}")

    # popping
    print()
    top_of_stack = stack.pop()
    print(f">> top: {top_of_stack}")
    print(stack)

    # pushing again
    print()
    stack.push("fourth")
    print(stack)

    # popping until empty
    print()
    while not stack.is_empty():
        print(f">> pop(): {stack.pop()}, peek(): {stack.peek() if not stack.is_empty() else '--empty stack--'}")
    print(stack)

    # pushing until full
    print()
    i = 0
    while not stack.is_full():
        stack.push(chr(ord('A') + i))
        i += 1
    print(stack)

    print("\n\n== HeapBackedStack")
    stack = HeapBackedStack()
    print(stack)

    # pushing first elem
    print()
    stack.push("first")
    print(stack)

    # pushing second elem
    print()
    stack.push("second")
    print(stack)

    # pushing third elem
    print()
    stack.push("third")
    print(stack)

    # peeking
    print()
    top_of_stack = stack.peek()
    print(f"top: {top_of_stack}")

    # popping
    print()
    top_of_stack = stack.pop()
    print(f">> top: {top_of_stack}")
    print(stack)

    # pushing again
    print()
    stack.push("fourth")
    print(stack)

    # popping until empty
    print()
    while not stack.is_empty():
        print(f">> pop(): {stack.pop()}, peek(): {stack.peek() if not stack.is_empty() else '--empty stack--'}")
    print(stack)

    # pushing until we have 10 elems in stack
    print()
    i = 0
    while len(stack) < 10:
        stack.push(chr(ord('A') + i))
        i += 1
    print(stack)
