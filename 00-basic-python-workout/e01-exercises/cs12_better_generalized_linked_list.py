from abc import ABC, abstractmethod


class LinkedList(ABC):

    class Node(ABC):

        def __init__(self, data, next=None):
            self._data = data
            self._next = next

        def __repr__(self):
            return f"(data={self._data}, next={self._next})"

        @abstractmethod
        def get_data(self):
            ...

        @abstractmethod
        def set_data(self, value):
            ...

        data = property(get_data, set_data, None)

        @abstractmethod
        def get_next(self):
            ...

        @abstractmethod
        def set_next(self, value):
            ...

        next = property(get_next, set_next, None)

    def __init__(self):
        self._head_ref = None

    def is_empty(self):
        return self._head_ref is None

    @abstractmethod
    def alloc_new_node(self, data, next):
        ...

    @abstractmethod
    def free_node_from_ref(self, p):
        ...

    @abstractmethod
    def node_from_ref(p):
        ...

    def _len(self):
        p = self._head_ref
        num_items = 0
        while p is not None:
            num_items += 1
            p = (self.node_from_ref(p)).next
        return num_items

    def __len__(self):
        return self._len()

    def insert(self, data, pos):
        if pos == 0:
            new_ref = self.alloc_new_node(data, self._head_ref)
            self._head_ref = new_ref
        elif pos > 0 and pos <= len(self):
            p = self._head_ref
            for _ in range(pos - 1):
                p = (self.node_from_ref(p)).next
            new_ref = self.alloc_new_node(data, (self.node_from_ref(p)).next)
            (self.node_from_ref(p)).next = new_ref
        else:
            raise ValueError(f"Invalid pos given for insertion: {pos}")

    def remove(self, pos):
        if self.is_empty():
            raise Exception("LinkedList is empty")

        if pos == 0:
            p = self._head_ref
            self._head_ref = (self.node_from_ref(self._head_ref)).next
            self.free_node_from_ref(p)
        elif pos > 0 and pos < len(self):
            p = self._head_ref
            for _ in range(pos - 1):
                p = (self.node_from_ref(p)).next
            q_node_ref_to_free = (self.node_from_ref(p)).next
            (self.node_from_ref(p)).next = self.node_from_ref((self.node_from_ref(p)).next).next
            self.free_node_from_ref(q_node_ref_to_free)
        else:
            raise ValueError(f"Invalid pos given for removal: {pos}")

    def __repr__(self) -> str:
        p = self._head_ref
        elems = []
        while p is not None:
            elems.append(str((self.node_from_ref(p)).data))
            p = (self.node_from_ref(p)).next
        comma_separated_elems = ", ".join(elems)
        return f"[{comma_separated_elems}]"

    @abstractmethod
    def is_full(self):
        ...

    def __iter__(self):
        p = self._head_ref
        while p is not None:
            yield self.node_from_ref(p).data
            p = self.node_from_ref(p).next


class HeapBackedLinkedList(LinkedList):

    class HeapBackedNode(LinkedList.Node):

        def get_data(self):
            return self._data

        def set_data(self, value):
            self._data = value

        data = property(get_data, set_data, None)

        def get_next(self):
            return self._next

        def set_next(self, value):
            self._next = value

        next = property(get_next, set_next, None)

    def alloc_new_node(self, data, next):
        return self.HeapBackedNode(data, next)

    def free_node_from_ref(self, p):
        p = None

    def node_from_ref(self, p):
        return p

    def is_full(self):
        return False


class ArrayBackedLinkedList(LinkedList):

    class ArrayBackedNode(LinkedList.Node):

        def __init__(self, data, next=None, storage=None, node_pos=None):
            if storage is None and node_pos is None:
                super().__init__(data, next)
                self.is_standalone = True
            elif storage is not None and node_pos is not None:
                self.is_standalone = False
                self.storage = storage
                self.node_pos = node_pos
            else:
                raise Exception("Unexpected state found while building an ArrayBackedNode")

        def get_data(self):
            if self.is_standalone:
                return self._data
            else:
                return self.storage[self.node_pos].data

        def set_data(self, value):
            if self.is_standalone:
                self._data = value
            else:
                self.storage[self.node_pos].data = value

        data = property(get_data, set_data, None)

        def get_next(self):
            if self.is_standalone:
                return self._next
            else:
                return self.storage[self.node_pos].next

        def set_next(self, value):
            if self.is_standalone:
                self._next = value
            else:
                self.storage[self.node_pos].next = value

        next = property(get_next, set_next, None)

    def __init__(self, max_size=10):
        super().__init__()
        self._max_size = max_size
        self._storage = self.init_storage()
        self._avail_head_ref = 0
        self._num_elems = 0

    def init_storage(self):
        storage = [self.ArrayBackedNode(None, i + 1) for i in range(0, self._max_size)]
        storage[-1].next = None
        return storage

    def alloc_new_node(self, data, next):
        p = self._avail_head_ref
        self._avail_head_ref = self._storage[self._avail_head_ref].next
        self._storage[p].data = data
        self._storage[p].next = next
        self._num_elems += 1
        return p

    def free_node_from_ref(self, p):
        self._storage[p].next = self._avail_head_ref
        self._avail_head_ref = p
        self._num_elems -= 1

    def node_from_ref(self, p):
        return self.ArrayBackedNode(None, None, self._storage, p)

    def is_full(self):
        return self._avail_head_ref is None


if __name__ == "__main__":
    print("Please run 'test_cs12_generalized_linked_list.py'")
