# IMPLEMENTATION OF QUEUE USING ARRAY

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.enqueue(20)
q.display()