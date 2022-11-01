

class DoublyLinkedList():
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def __repr__(self):
            return f"(data={self.data}, prev={self.prev}, next={self.next})"

    def __init__(self):
        self.head = None
        self.num_items = 0

    def is_empty(self):
        return self.head is None

    def __len(self):
        return self.num_items

    def insert(self, data, pos):
        if pos < 0 or pos > self.num_items:
            raise AttributeError("pos argument is out of bounds for inserting")

        if self.head is None:
            p = self.Node(data)
            self.head = p
        elif pos == 0:
            p = self.head
            q = self.Node(data)
            q.next = p
            q.prev = p.prev
            p.prev = q
            self.head = q
        else:
            p = self.head
            for _ in range(pos - 1):
                p = p.next
            q = self.Node(data)
            q.next = p.next
            p.next = q
            q.prev = p
            if q.next is not None:
                q.next.prev = q
        self.num_items += 1

    def remove(self, pos):
        if pos < 0 or pos >= self.num_items:
            raise AttributeError("pos argument is out of bounds for removing")

        if pos == 0:
            p = self.head
            self.head = self.head.next
            p.prev = None
            p.next = None
            if self.head is not None:
                self.head.prev = None
        else:
            p = self.head
            for _ in range(pos - 1):
                p = p.next
            q = p.next
            p.next = q.next
            if q.next is not None:
                q.next.prev = p
            q.prev = None
            q.next = None
        self.num_items -= 1

    def find_by_pos(self, pos):
        if pos < 0 or pos >= self.num_items:
            raise AttributeError("pos argument is out of bounds for finding")

        p = self.head
        for _ in range(pos):
            p = p.next
        return p

    def find_by_data(self, data):
        p = self.head
        while p is not None and p.data != data:
            p = p.next
        return p

    def __repr__(self) -> str:
        if self.head is None:
            return "[]"
        else:
            elems = [str(data) for data in self]
            comma_separated_elems = ", ".join(elems)
            return f"[{comma_separated_elems}]"

    def __iter__(self):
        p = self.head
        while p is not None:
            yield p.data
            p = p.next

    def __len__(self):
        return self.__len()


if __name__ == "__main__":
    print("Please run test_cs18_doubly_linked_list.py")