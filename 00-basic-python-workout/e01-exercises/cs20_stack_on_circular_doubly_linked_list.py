from cs19_circular_doubly_linked_list import CircularDoublyLinkedList


class Stack(CircularDoublyLinkedList):

    def push(self, elem):
        self.insert(elem, 0)

    def pop(self):
        if self.num_items == 0:
            raise Exception("Cannot pop from empty stack")

        top_of_stack = self.tail.next.data
        self.remove(0)
        return top_of_stack

    def peek(self):
        if self.num_items == 0:
            raise Exception("Cannot peek on empty stack")

        top_of_stack = self.tail.next.data
        return top_of_stack

    def __repr__(self):
        if self.is_empty():
            return "-- empty stack --"
        elems_str = [f"{i}: {elem}" for (elem, i) in zip(self, range(len(self)))]
        return "\n".join(reversed(elems_str))


if __name__ == "__main__":
    print("Please run test_cs20_stack_on_circular_doubly_linked_list.py")