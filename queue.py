class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)


# 큐 테스트
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())
print("Removed item from queue:", queue.dequeue())
print("Queue size after dequeue:", queue.size())
print("Removed item from queue:", queue.dequeue())

if queue.is_empty():
    print('queue is empty')
else :
    print('queue is full')