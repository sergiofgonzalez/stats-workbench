from cs15_circular_list import CircularList


class Queue(CircularList):
    def enqueue(self, elem):
        self.insert(elem, len(self))

    def dequeue(self):
        head_elem = self.head()
        self.remove(0)
        return head_elem

    def head(self):
        if self.tail is None:
            raise Exception("Cannot read head of empty queue")

        return self.tail.next.data

    def __iter__(self):
        if self.tail is None:
            return None

        head_marker = self.tail.next
        p = self.tail.next
        done = False
        while not done:
            yield p.data
            p = p.next
            done = True if p == head_marker else False


if __name__ == "__main__":
    print("Please run test_cs16_queue_on_circular_list.py")