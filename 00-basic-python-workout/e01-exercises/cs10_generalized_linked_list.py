from abc import ABC, abstractmethod


# note that I have modified some `__methods` and `__property` by a single underscore to prevent name-mangling and
# facilitate the access from the subclass

class LinkedList(ABC):

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    @abstractmethod
    def _len(self):
        ...

    def __len__(self):
        return self._len()

    @abstractmethod
    def insert(self, data, pos):
        ...

    @abstractmethod
    def remove(self, pos):
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...

    @abstractmethod
    def is_full(self):
        ...

    @abstractmethod
    def __iter__(self):
        ...


class HeapBackedLinkedList(LinkedList):
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        def __repr__(self):
            return f"(data={self.data}, next={self.next})"

    def _len(self):
        num_nodes = 0
        p = self._head
        while p is not None:
            num_nodes += 1
            p = p.next
        return num_nodes

    def insert(self, data, pos):
        if pos == 0:
            node = self.Node(data, self._head)
            self._head = node
        elif pos > 0 and pos <= self._len():
            p = self._head
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
            self._head = self._head.next
        elif pos > 0 and pos < self._len():
            p = self._head
            for _ in range(pos - 1):
                p = p.next
            p.next = p.next.next
        else:
            raise ValueError(f"Invalid pos given for removal: {pos}")

    def __repr__(self) -> str:
        if self.is_empty():
            return "[]"
        else:
            p = self._head
            elems = [p.data]
            while p.next is not None:
                p = p.next
                elems.append(str(p.data))
            comma_separated_elems = ", ".join(elems)
            return f"[{comma_separated_elems}]"

    def is_full(self):
        return False

    def __iter__(self):
        p = self._head
        while p is not None:
            yield p.data
            p = p.next


class ArrayBackedLinkedList(LinkedList):

    def __init__(self, max_size=10):
        super().__init__()
        self._max_size = max_size
        self._storage = self.__init_storage()
        self._avail_head = 0
        self._num_elems = 0

    def __init_storage(self):
        storage = [{"data": None, "next": i + 1} for i in range(0, self._max_size)]
        storage[-1]["next"] = None
        return storage

    def _len(self):
        return self._num_elems

    def insert(self, data, pos):
        if self.is_full():
            raise Exception("ArrayBackedLinkedList is full")

        if pos == 0:
            p = self._avail_head
            self._avail_head = self._storage[self._avail_head]["next"]
            self._storage[p]["data"] = data
            self._storage[p]["next"] = self._head
            self._head = p
            self._num_elems += 1
        elif pos > 0 and pos <= self._num_elems:
            p = self._avail_head
            self._avail_head = self._storage[self._avail_head]["next"]
            self._storage[p]["data"] = data
            q = self._head
            for _ in range(0, pos - 1):
                q = self._storage[q]["next"]
            self._storage[p]["next"] = self._storage[q]["next"]
            self._storage[q]["next"] = p
            self._num_elems += 1
        else:
            raise ValueError(f"Invalid pos given for insertion: {pos}")

    def remove(self, pos):
        if self.is_empty():
            raise Exception("ArrayBackedLinkedList is empty")

        if pos == 0:
            p = self._head
            self._head = self._storage[p]["next"]
            self._storage[p]["next"] = self._avail_head
            self._avail_head = p
            self._num_elems -= 1
        elif pos > 0 and pos < self._num_elems:
            p = self._head
            for _ in range(0, pos - 1):
                p = self._storage[p]["next"]
            q = self._storage[p]["next"]
            self._storage[p]["next"] = self._storage[q]["next"]
            self._storage[q]["next"] = self._avail_head
            self._avail_head = q
            self._num_elems -= 1
        else:
            raise ValueError(f"Invalid pos given for removal: {pos}")

    def __repr__(self) -> str:
        if self.is_empty():
            return "[]"
        else:
            p = self._head
            elems = [self._storage[p]["data"]]
            while self._storage[p]["next"] is not None:
                p = self._storage[p]["next"]
                elems.append(str(self._storage[p]["data"]))
            comma_separated_elems = ", ".join(elems)
            return f"[{comma_separated_elems}]"

    def is_full(self):
        return self._avail_head is None

    def __iter__(self):
        p = self._head
        while p is not None:
            yield self._storage[p]["data"]
            p = self._storage[p]["next"]


if __name__ == "__main__":
    print("Please run 'test_cs10_generalized_linked_list.py'")
