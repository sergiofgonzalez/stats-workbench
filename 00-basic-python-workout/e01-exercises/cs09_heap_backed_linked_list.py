
class HeapBackedLinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        def __repr__(self):
            return f"(data={self.data}, next={self.next})"

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def __len(self):
        num_nodes = 0
        p = self.__head
        while p is not None:
            num_nodes += 1
            p = p.next
        return num_nodes

    def insert(self, data, pos):
        if pos == 0:
            node = self.Node(data, self.__head)
            self.__head = node
        elif pos > 0 and pos <= self.__len():
            p = self.__head
            for _ in range(pos - 1):
                p = p.next
            node = self.Node(data, p.next)
            p.next = node
        else:
            raise ValueError(f"Invalid pos given for insertion: {pos}")

    def remove(self, pos):
        if self.is_empty():
            raise Exception("HeapBackedLinkedList is empty")

        if pos == 0:
            self.__head = self.__head.next
        elif pos > 0 and pos < self.__len():
            p = self.__head
            for _ in range(pos - 1):
                p = p.next
            p.next = p.next.next
        else:
            raise ValueError(f"Invalid pos given for removal: {pos}")

    def __repr__(self) -> str:
        if self.is_empty():
            return "[]"
        else:
            p = self.__head
            elems = [p.data]
            while p.next is not None:
                p = p.next
                elems.append(str(p.data))
            comma_separated_elems = ", ".join(elems)
            return f"[{comma_separated_elems}]"

    def is_full(self):
        return False

    def __iter__(self):
        p = self.__head
        while p is not None:
            yield p.data
            p = p.next

    def __len__(self):
        return self.__len()


if __name__ == "__main__":
    print("Please run 'test_cs09_heap_backed_linked_list.py'")
