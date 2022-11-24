from cs19_circular_doubly_linked_list import CircularDoublyLinkedList


class Queue(CircularDoublyLinkedList):

    def enqueue(self, elem):
        self.insert(elem)

    def insert(self, elem):
        super().insert(elem, self.num_items)

    def dequeue(self):
        return self.remove()

    def remove(self):
        if self.num_items == 0:
            raise Exception("Cannot dequeue on an empty queue")

        head_elem = self.find_by_pos(0)
        super().remove(0)
        return head_elem.data


if __name__ == "__main__":
    print("Please run test_cs21_stack_on_circular_doubly_linked_list.py")