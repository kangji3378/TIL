class Array:
    CAPACITY = 10
    def __init__(self, capacity=CAPACITY):
        self.items = [None] * capacity
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    def __getitem__(self, index):
        return self.items[index]
    def __setitem__(self, index, item):
        self.items[index] = item
class Queue:
    CAPACITY = 10
    def __init__(self, capacity=CAPACITY):
        self.arr = Array(capacity)
        self.capacity = capacity
        self.front = self.rear = -1
    def is_full(self):
        if self.rear+1==self.capacity:
            return True
        else:
            return False
    def is_empty(self):
        if self.rear==self.front:
            self.rear=-1
            self.front=-1
            return True
        else:
            return False
    def enqueue(self, elem):
        if self.is_full():
            raise Exception("queue is full")
        else:
            self.arr[self.rear+1]=elem
            self.rear+=1
    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty")
        else:
            self.arr[self.front+1]=None
            self.front+=1
    def peek(self):
        if self.is_empty():
            raise Exception("queue is empty")
        else:
            return self.arr[self.front+1]
    def __len__(self):
        return self.rear-self.front
    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.arr[pos]
            pos += 1
    def __str__(self):
        return str(self.arr)

N = 5
q = Queue(N)
print("Length:", len(q))
print("Empty:", q.is_empty())
print("Enqueue 1-", N)
for i in range(1, N + 1):
    q.enqueue(i)
    print("Peeking:", q.peek())
    print("Queue =", q)
print("Length:", len(q))
print("Empty:", q.is_empty())
while not q.is_empty(): 
    print("Peeking:", q.peek())
    q.dequeue()
    print("Queue =", q)
print("Length:", len(q))
print("Empty:", q.is_empty())