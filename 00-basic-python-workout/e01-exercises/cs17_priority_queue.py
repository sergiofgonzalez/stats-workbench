from cs15_circular_list import CircularList


class PriorityQueue():
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

        def __repr__(self):
            return f"(data={self.data}, next={self.next})"

    @staticmethod
    def defaultPriorityFn(x, y):
        if x < y:
            return -1
        elif x == y:
            return 0
        else:
            return 1

    def __init__(self, priorityFn=None):
        self.tail = None
        self.num_items = 0
        if priorityFn is None:
            self.priorityFn = PriorityQueue.defaultPriorityFn
        else:
            self.priorityFn = priorityFn

    def is_empty(self):
        return self.tail is None

    def __len(self):
        return self.num_items

    def insert(self, data):
        if self.tail is None:
            p = self.Node(data)
            p.next = p
            self.tail = p
        else:
            if self.priorityFn(data, self.tail.data) >= 0:
                p = self.Node(data, self.tail.next)
                q = self.tail
                self.tail = p
                q.next = p
            else:
                p = self.tail
                while self.priorityFn(data, p.next.data) > 0:
                    p = p.next
                q = self.Node(data, p.next)
                p.next = q
        self.num_items += 1

    def __contains__(self, elem):
        if self.tail is None:
            return False
        else:
            if self.priorityFn(elem, self.tail.data) > 0:
                return False
            elif self.priorityFn(elem, self.tail.data) == 0:
                return True
            else:
                p = self.tail.next
                while self.priorityFn(elem, p.data) > 0:
                    p = p.next
                if self.priorityFn(elem, p.data) == 0:
                    return True
                else:
                    return False

    def remove(self, elem):
        if self.tail is None:
            return False
        elif self.priorityFn(elem, self.tail.data) > 0:
            return False
        elif self.num_items == 1 and self.priorityFn(elem, self.tail.data) == 0:
            self.num_items = 0
            self.tail = None
            return True
        else:
            p = self.tail
            while self.priorityFn(elem, p.next.data) > 0:
                p = p.next
            if self.priorityFn(elem, p.next.data) == 0:
                if p.next == self.tail:
                    self.tail = p
                p.next = p.next.next
                self.num_items -= 1
                return True
            else:
                return False

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
        elif self.num_items == 1:
            yield self.tail.data
        else:
            p = self.tail.next
            while p.next != self.tail.next:
                yield p.data
                p = p.next
            yield self.tail.data

    def __len__(self):
        return self.__len()


if __name__ == "__main__":
    print("Please run test_cs17_priority_queue.py")