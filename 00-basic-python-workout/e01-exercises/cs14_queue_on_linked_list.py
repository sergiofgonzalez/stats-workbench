from cs12_better_generalized_linked_list import LinkedList, ArrayBackedLinkedList, HeapBackedLinkedList


class Queue(LinkedList):

    def enqueue(self, item):
        self.insert(item, len(self))

    def dequeue(self):
        head = (self.node_from_ref(self._head_ref)).data
        self.remove(0)
        return head

    def __repr__(self) -> str:
        if self.is_empty():
            return "-- empty queue --"
        elems_str = [f"{i}: {elem}" for (elem, i) in zip(self, range(len(self)))]
        return "\n".join(elems_str)


class ArrayBackedQueue(Queue, ArrayBackedLinkedList):
    ...


class HeapBackedQueue(Queue, HeapBackedLinkedList):
    ...


if __name__ == "__main__":
    q = ArrayBackedQueue()
    print("== ArrayBackedQueue")

    print("\n=== empty queue")
    print(q.is_empty())
    print(q)

    print("\n=== queue with single elem")
    q.enqueue('a')
    print(q.is_empty())
    print(q)

    print("\n=== dequeuing")
    q.enqueue('b')
    print(q)
    head = q.dequeue()
    print(f"head: {head}")
    print(q)

    print("\n\n== HeapBackedQueue")

    q = HeapBackedQueue()

    print("\n=== empty queue")
    print(q.is_empty())
    print(q)

    print("\n=== queue with single elem")
    q.enqueue('a')
    print(q.is_empty())
    print(q)

    print("\n=== dequeuing")
    q.enqueue('b')
    print(q)
    head = q.dequeue()
    print(f"head: {head}")
    print(q)
