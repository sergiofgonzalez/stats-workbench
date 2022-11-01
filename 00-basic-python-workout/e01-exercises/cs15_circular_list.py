class CircularList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        def __repr__(self):
            return f"(data={self.data}, next={self.next})"

    def __init__(self):
        self.tail = None
        self.num_items = 0

    def is_empty(self):
        return self.tail is None

    def __len(self):
        return self.num_items

    def insert(self, data, pos):
        if pos == 0:
            node = self.Node(data)
            if self.tail is None:
                self.tail = node
                node.next = self.tail
            else:
                node.next = self.tail.next
                self.tail.next = node
            self.num_items += 1
        elif pos > 0 and pos <= self.num_items:
            p = self.tail.next
            for _ in range(pos - 1):
                p = p.next
            node = self.Node(data, p.next)
            p.next = node
            if pos == self.num_items:
                self.tail = node
            self.num_items += 1
        else:
            raise ValueError(f"Invalid pos given for insertion: {pos}")

    def remove(self, pos):
        if pos < 0 or pos > self.num_items - 1:
            raise ValueError(f"Invalid pos given for removal: {pos}")
        if self.num_items == 1:
            self.tail = None
            self.num_items -= 1
        else:
            p = self.tail
            for _ in range(pos):
                p = p.next
            q = p.next
            p.next = q.next
            if pos == self.num_items - 1:
                self.tail = p
            self.num_items -= 1

    def __repr__(self) -> str:
        if self.tail is None:
            return "[]"
        else:
            p = self.tail.next
            elems = [p.data]
            while p != self.tail:
                p = p.next
                elems.append(str(p.data))
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
    print("Please run 'test_cs15_circular_list.py'")
