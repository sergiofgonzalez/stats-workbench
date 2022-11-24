
from abc import ABC, abstractmethod


class Option(ABC):

    @abstractmethod
    def has_value(self):
        ...

    @abstractmethod
    def get(self):
        ...

    def get_or_else(self, alt_value):
        return self.get() if self.has_value() else alt_value


class Some(Option):
    def __init__(self, value):
        self.value = value

    def has_value(self):
        return True

    def get(self):
        return self.value

    def __eq__(self, other):
        if other is None or other.__class__ != Some.__class__:
            return False
        else:
            return self.value == other.get()

    def __repr__(self):
        return f"Some({self.value})"


class Empty(Option):

    def has_value(self):
        return False

    def get(self):
        raise Exception("Empty")

    def __eq__(self, other):
        if other is None or other.__class__ != Empty.__class__:
            return False
        else:
            return True

    def __repr__(self):
        return "Empty()"


def wrap(value: object) -> Option:
    if value is None:
        return Empty()
    else:
        return Some(value)


if __name__ == "main":
    print(f"Please run test_cs28_option.py")
