from typing import Any, List, Dict, Optional, Sequence, Tuple, TypedDict, Callable

# forcing an err
x: int = 2

# reported as error but runs
x = "Hello"

print(x)


# complex list types: example 1
def my_fn(nums: List[float]) -> float:
    return sum(nums)


print(my_fn([1.1, 2.2, 3.3]))


# complex list types: example 2
NestedList = List[List[str]]

my_list: NestedList = [["hello", "to"], ["Jason"]]

print(my_list)

# complex dict types
KeyValueType = Dict[str, float]

my_dict: KeyValueType = {"num_1": 3.25, "num_2": 5.75}

print(my_dict)


# TypedDicts: dicts with fixed schema
class InterestsTypedDict(TypedDict):
    name: str
    interests: List[str]


my_interests: InterestsTypedDict = {"name": "sergio", "interests": ["movies", "stuff"]}

print(my_interests)


# Arguments that are functions: dummy callable
def sum_numbers(x: int, y: int) -> int:
    return x + y


def oper(x: int, y: int, fn: Callable) -> int:
    return fn(x, y)


print(oper(2, 3, sum_numbers))


# Arguments that are functions: better annotations
def oper_2(x: int, y: int, fn: Callable[[int, int], int]) -> int:
    return fn(x, y)


print(oper(2, 3, sum_numbers))


# Using `Any`
def foo(x: Any) -> None:
    print(x)


foo(2)
foo("hello")


# Optional params
def bar(x: Optional[int] = 5) -> int:
    if (x):
        return x * 2
    else:
        return -1


print(bar(5))
print(bar())


# Sequence
def print_sequence_elems(sequence: Sequence[str]):
    for i, s in enumerate(sequence):
        print(f"{i}: {s}")


print_sequence_elems(["a", "b", "c"])


# Typed and non-typed tuples

# non-typed tuple
t: tuple = (1, 2, 3, "catorce")

# typed tuple
t_2: Tuple[int, int, int, str] = (1, 2, 3, "catorce")
