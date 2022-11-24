from abc import ABC, abstractmethod


class List(ABC):

    @abstractmethod
    def head(self):
        ...

    @abstractmethod
    def tail(self):
        ...

    def is_empty(self):
        ...

    def search(self, elem):
        def do_recursive_search(ll):
            if ll == EMPTY:
                return None
            elif ll.head() == elem:
                return elem
            else:
                return do_recursive_search(ll.tail())

        return do_recursive_search(self)

    @staticmethod
    def create_from_elems(*elems):
        if len(elems) == 0:
            return EMPTY
        else:
            head = elems[0]
            tail = List.create_from_elems(*elems[1:])
            return _NonEmptyList(head, tail)

    @staticmethod
    def list(head, tail):
        return _NonEmptyList(head, tail)

    @staticmethod
    def empty_list():
        return EMPTY


class _NonEmptyList(List):
    def __init__(self, head: object, tail: List) -> None:
        self._head = head
        self._tail = tail

    def head(self) -> object:
        return self._head

    def tail(self) -> List:
        return self._tail

    def __repr__(self) -> str:
        return f"({self.head()}, {self.tail()})"

    def __eq__(self, other) -> bool:
        if other is None or self.__class__ != other.__class__:
            return False
        else:
            return self.head() == other.head() and self.tail() == other.tail()


class _Empty(List):
    def head(self):
        raise Exception("empty list has no head")

    def tail(self):
        raise Exception("empty list has no tail")

    def __repr__(self):
        return "()"


EMPTY = _Empty()


if __name__ == "__main__":
    print("Please run test_cs30_list_recursive_data_type")
