from cs10_generalized_linked_list import LinkedList, HeapBackedLinkedList, ArrayBackedLinkedList


class CloneableArrayBackedLinkedList(ArrayBackedLinkedList):
    def clone(self):
        cloned_list = ArrayBackedLinkedList(self._max_size)
        for i in range(len(self)):
            cloned_list.insert(self._storage[i]["data"], i)
        return cloned_list


class CloneableHeapBackedLinkedList(HeapBackedLinkedList):
    def clone(self):
        cloned_list = HeapBackedLinkedList()

        for (data, i) in zip(self, range(len(self))):
            cloned_list.insert(data, i)
        return cloned_list


if __name__ == "__main__":
    print("== Cloning Linked Lists ==")

    print("\n1. Array backed")
    ll_1 = CloneableArrayBackedLinkedList(max_size=26)
    for i in range(26):
        ll_1.insert(chr(ord('A') + i), i)
    ll_2 = ll_1.clone()

    # should be equal
    print(f"{ll_1}\n{ll_2}\n")

    # ll_1 should be missing 'A'
    ll_1.remove(0)
    print(f"{ll_1}\n{ll_2}\n")

    # ll_2 should be missing 'B'
    ll_2.remove(len(ll_2) - 1)
    print(f"{ll_1}\n{ll_2}\n")

    print("\n2. Heap backed")
    ll_3 = CloneableHeapBackedLinkedList()
    for i in range(26):
        ll_3.insert(chr(ord('A') + i), i)
    ll_4 = ll_3.clone()

    # should be equal
    print(f"{ll_1}\n{ll_2}\n")

    # ll_1 should be missing 'A'
    ll_1.remove(0)
    print(f"{ll_1}\n{ll_2}\n")

    # ll_2 should be missing 'B'
    ll_2.remove(len(ll_2) - 1)
    print(f"{ll_1}\n{ll_2}\n")
