class Queue:
    def __init__(self, len):
        self.queue = []
        self.len = len

    def enqueue(self, val):
        if len(self.queue) <= self.len:
            self.queue.append(val)
        else:
            print("Overflow")

    def dequeue(self):
        if len(self.queue) <= 0:
            print("Empty Queue!!!")
        else:
            print(self.queue.pop(0))

    def display(self):
        if len(self.queue) > 0:
            print(self.queue)
        else:
            print("Empty Queue!!!!")

q = Queue(5)
for index in range(5):
    q.enqueue(index)
q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.display()
