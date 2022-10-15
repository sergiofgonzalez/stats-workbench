

class ArrayBackedLinkedList:

    def __init__(self, max_size=10):
        self.__max_size = max_size
        self.__head = None
        self.__storage = self.__init_storage()
        self.__avail_head = 0
        self.__num_elems = 0

    def __init_storage(self):
        storage = [{"data": None, "next": i + 1} for i in range(0, self.__max_size)]
        storage[-1]["next"] = None
        return storage

    def is_empty(self):
        return self.__head is None

    def len(self):
        return self.__num_elems

    def insert(self, data, pos):
        if self.is_full():
            raise Exception("ArrayBackedLinkedList is full")

        if pos == 0:
            p = self.__avail_head
            self.__avail_head = self.__storage[self.__avail_head]["next"]
            self.__storage[p]["data"] = data
            self.__storage[p]["next"] = self.__head
            self.__head = p
            self.__num_elems += 1
        elif pos > 0 and pos <= self.__num_elems:
            p = self.__avail_head
            self.__avail_head = self.__storage[self.__avail_head]["next"]
            self.__storage[p]["data"] = data
            q = self.__head
            for _ in range(0, pos - 1):
                q = self.__storage[q]["next"]
            self.__storage[p]["next"] = self.__storage[q]["next"]
            self.__storage[q]["next"] = p
            self.__num_elems += 1
        else:
            raise ValueError(f"Invalid pos given for insertion: {pos}")

    def remove(self, pos):
        if self.is_empty():
            raise Exception("ArrayBackedLinkedList is empty")

        if pos == 0:
            p = self.__head
            self.__head = self.__storage[p]["next"]
            self.__storage[p]["next"] = self.__avail_head
            self.__avail_head = p
            self.__num_elems -= 1
        elif pos > 0 and pos < self.__num_elems:
            p = self.__head
            for _ in range(0, pos - 1):
                p = self.__storage[p]["next"]
            q = self.__storage[p]["next"]
            self.__storage[p]["next"] = self.__storage[q]["next"]
            self.__storage[q]["next"] = self.__avail_head
            self.__avail_head = q
            self.__num_elems -= 1
        else:
            raise ValueError(f"Invalid pos given for removal: {pos}")

    def __repr__(self) -> str:
        if self.is_empty():
            return "[]"
        else:
            p = self.__head
            elems = [self.__storage[p]["data"]]
            while self.__storage[p]["next"] is not None:
                p = self.__storage[p]["next"]
                elems.append(str(self.__storage[p]["data"]))
            comma_separated_elems = ", ".join(elems)
            return f"[{comma_separated_elems}]"

    def is_full(self):
        return self.__avail_head is None

    def __iter__(self):
        p = self.__head
        while p is not None:
            yield self.__storage[p]["data"]
            p = self.__storage[p]["next"]

    def __len__(self):
        return self.len()

# # Uncomment to run a shakedown test
# if __name__ == "__main__":
#     print("== Array-backed linked list shakedown")
#     print()

#     # initializing the list
#     ll = ArrayBackedLinkedList(max_size=3)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # trying to remove from empty list should fail
#     try:
#         ll.remove(0)
#     except Exception as err:
#         print(f"Error caught: {err}")
#     print()

#     # inserting a first element
#     ll.insert('a', 0)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # removing first element from a list with a single element
#     ll.remove(0)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # inserting a second element in the first pos
#     ll.insert('a', 0)

#     ll.insert('b', 0)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # removing first element from a list with 2 elements
#     ll.remove(0)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # inserting a third element in the first pos
#     ll.insert('b', 0)

#     ll.insert('c', 0)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll.is_full()={ll.is_full()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # try inserting a fourth element should fail
#     try:
#         ll.insert('will fail', 0)
#     except Exception as err:
#         print(f"Error caught: {err}")
#     print()

#     # removing first element from a list with 3 elements
#     ll.remove(0)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # insert element in the second position in a list with 2 elements
#     ll.insert('X', 1)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll.is_full()={ll.is_full()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # insert element in the third position in a list with 2 elements
#     ll.remove(0)

#     ll.insert('Z', 2)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll.is_full()={ll.is_full()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # insert elements in the last position until full
#     ll.remove(0)
#     ll.remove(0)
#     ll.remove(0)

#     ll.insert('a', ll.len())
#     ll.insert('b', ll.len())
#     ll.insert('c', ll.len())
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll.is_full()={ll.is_full()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # insert elements in the first position until full
#     ll.remove(0)
#     ll.remove(0)

#     ll.insert('Y', 1)
#     ll.insert('X', 1)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll.is_full()={ll.is_full()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # insert elements in the last position until full
#     ll.remove(0)
#     ll.remove(0)
#     ll.remove(0)

#     ll.insert('a', ll.len())
#     ll.insert('b', ll.len())
#     ll.insert('c', ll.len())
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll.is_full()={ll.is_full()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # remove element in the second position in list with 3 elements
#     ll.remove(1)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll.is_full()={ll.is_full()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # remove element in the second position in list with 2 elements
#     ll.remove(1)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll.is_full()={ll.is_full()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # remove elements in the last position until empty
#     ll.insert('x', 0)
#     ll.insert('e', ll.len())

#     ll.remove(ll.len() - 1)
#     ll.remove(ll.len() - 1)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll.is_full()={ll.is_full()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     ll.remove(ll.len() - 1)
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll.is_full()={ll.is_full()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # trying to insert beyond limits (neg pos)
#     try:
#         ll.insert('X', -1)
#     except Exception as err:
#         print(f"Error caught: {err}")
#     print()

#     # trying to insert beyond limits on empty list (post len)
#     try:
#         ll.insert('X', ll.len() + 1)
#     except Exception as err:
#         print(f"Error caught: {err}")
#     print()

#     # trying to insert beyond limits on non-empty/non-full list (post len)
#     ll.insert('a', 0)
#     ll.insert('b', 1)

#     try:
#         ll.insert('X', ll.len() + 1)
#     except Exception as err:
#         print(f"Error caught: {err}")
#     print()

#     # trying to insert beyond limits on full list (post len)
#     ll.insert('c', ll.len())

#     try:
#         ll.insert('X', ll.len() + 1)
#     except Exception as err:
#         print(f"Error caught: {err}")
#     print()

#     # trying to remove beyond limits (neg pos)
#     try:
#         ll.remove(-1)
#     except Exception as err:
#         print(f"Error caught: {err}")
#     print()

#     # trying to remove beyond limits (post len)
#     try:
#         ll.remove(ll.len())
#     except Exception as err:
#         print(f"Error caught: {err}")
#     print()

#     # inserting in the len(ll) pos on a non-full list
#     ll.remove(0)

#     ll.insert('a', ll.len())
#     print(f"ll.is_empty()={ll.is_empty()}")
#     print(f"ll.is_full()={ll.is_full()}")
#     print(f"ll(len): {ll.len()}")
#     print(f"ll={ll}")
#     print()

#     # inserting in the len(ll) pos on a full list
#     try:
#         ll.insert('Z', ll.len())
#     except Exception as err:
#         print(f"Error caught: {err}")
#     print()

#     # __iter__
#     for elem in ll:
#         print(f"elem={elem}")

#     # __len__
#     print(f"len(ll)={len(ll)}")
