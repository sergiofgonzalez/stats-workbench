
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        head = self.items.pop(0)
        return head

    def __repr__(self) -> str:
        return self.items.__repr__()


q = Queue()

print("=== empty queue")
print(q.is_empty())
print(q)

print("\n=== queue with single elem")
q.enqueue('a')
print(q.is_empty())
print(q)


print("\n=== dequeuing")
q.enqueue('b')
print(q)
head = q.dequeue()
print(f"head: {head}")
print(q)
