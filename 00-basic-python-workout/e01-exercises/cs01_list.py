my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
another_list = list([2, 4, 6, 8])
empty_list = []
another_empty_list = list()


def is_empty(list):
    return len(list) == 0


print("=== is_empty")
print(f"is_empty(my_list)={is_empty(my_list)}")
print(f"is_empty(another_list)={is_empty(another_list)}")
print(f"is_empty(empty_list)={is_empty(empty_list)}")
print(f"is_empty(another_empty_list)={is_empty(another_empty_list)}")


def insert(list, elem, pos):
    list.insert(elem, pos)
    return list


print("=== insert(elem, pos)")
insert(empty_list, 0, 0)
print(empty_list)
insert(another_list, 2, 5)
print(another_list)
insert(my_list, 10, 10)
print(my_list)


def remove(list, pos):
    elem = list[pos]
    list.remove(elem)


print("=== remove(pos)")
remove(empty_list, 0)
print(empty_list)
remove(another_list, 2)
print(another_list)
remove(my_list, 10)
print(my_list)


def traverse(a_list, fn):
    return list(map(fn, a_list))


def traverse_inline(list, fn):
    for i in range(0, len(list)):
        list[i] = fn(list[i])


print("=== insert(elem, pos)")
traversedList = traverse(my_list, lambda n: n * 2)
print(list(traversedList))
