class Queue:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def enqueue(self, item):
        self.item.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)
        else:
            return None
    def size(self):
        return len(self.item)


