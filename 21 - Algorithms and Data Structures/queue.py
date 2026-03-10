class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        # return self.items.pop(0)
        head = self.items[0]
        self.items = self.items[1:]
        return head


q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q.items)

print(q.pop())
print(q.items)

print(q.pop())
print(q.items)

print(q.pop())
print(q.items)
