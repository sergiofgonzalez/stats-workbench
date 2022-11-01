
class CircularDoublyLinkedList():
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def __repr__(self):
            return f"(data={self.data}, prev={self.prev}, next={self.next})"

    def __init__(self):
        self.tail = None
        self.num_items = 0

    def is_empty(self):
        return self.tail is None

    def __len(self):
        return self.num_items

    def insert(self, data, pos):
        if pos < 0 or pos > self.num_items:
            raise AttributeError("pos argument is out of bounds for inserting")

        if self.tail is None:
            p = self.Node(data)
            p.next = p
            p.prev = p
            self.tail = p
        elif pos == self.num_items:
            p = self.tail
            q = self.Node(data)
            q.next = p.next
            q.prev = p
            p.next = q
            q.next.prev = q
            self.tail = q
        else:
            p = self.tail
            for _ in range(pos):
                p = p.next
            q = self.Node(data)
            q.next = p.next
            p.next = q
            q.prev = p
            q.next.prev = q
        self.num_items += 1

    def remove(self, pos):
        if pos < 0 or pos >= self.num_items:
            raise AttributeError("pos argument is out of bounds for removing")

        if pos == self.num_items - 1:
            p = self.tail
            if self.num_items == 1:
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = p.next
            p.prev = None
            p.next = None
        else:
            p = self.tail
            for _ in range(pos):
                p = p.next
            q = p.next
            p.next = q.next
            q.next.prev = p
            q.prev = None
            q.next = None
        self.num_items -= 1

    def find_by_pos(self, pos):
        if pos < 0 or pos >= self.num_items:
            raise AttributeError("pos argument is out of bounds for finding")

        p = self.tail.next
        for _ in range(pos):
            p = p.next
        return p

    def find_by_data(self, data):
        if self.tail is None:
            return None
        else:
            p = self.tail
            if p.data == data:
                return p
            else:
                p = p.next
                while p != self.tail and p.data != data:
                    p = p.next
                if p == self.tail:
                    return None
                else:
                    return p

    def __repr__(self) -> str:
        if self.tail is None:
            return "[]"
        else:
            elems = []
            p = self.tail.next
            for _ in range(self.num_items):
                elems.append(str(p.data))
                p = p.next
            comma_separated_elems = ", ".join(elems)
            return f"[{comma_separated_elems}]"

    def __iter__(self):
        if self.tail is None:
            yield from []
        else:
            p = self.tail.next
            while True:
                yield p.data
                p = p.next

    def __len__(self):
        return self.__len()


if __name__ == "__main__":
    print("Please run test_cs19_circular_doubly_linked_list.py")