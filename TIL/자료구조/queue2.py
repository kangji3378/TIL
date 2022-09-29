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
        self.capacity = capacity
        self.arr = Array(self.capacity)
        self.front = self.rear = -1
    def is_empty(self):
        return self.front == -1 and self.rear == -1
    def is_full(self):
        return self.front!=-1 and self.rear+1==self.front
    def peek(self):
        if self.is_empty():
            raise Exception("queue is empty.")
        return self.arr[self.front]
    def __len__(self):
        if self.is_empty():
            return 0
        if self.rear<self.front:
            return self.capacity-self.front+self.rear+1
        return self.rear-self.front+1
    def __str__(self):
        return str(self.arr)
    def __iter__(self):
        pos=self.front
        for i in range(pos,pos+len(self)):
            yield self.arr[i%self.capacity]
    def enqueue(self, elem):
        if self.is_full():
            raise Exception("queue is full")
        else:
            self.rear=(self.rear+1)%self.capacity
            self.arr[self.rear%self.capacity]=elem
            if self.front==-1:
                self.front=0
    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty")
        self.arr[self.front%self.capacity]=None
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
            return
        self.front=(self.front+1)%self.capacity
N = 8
queue = Queue(N)
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.enqueue("D")
print(queue)
print("Peek:", queue.peek())
queue.dequeue()
print("Peek:", queue.peek())
queue.dequeue()
print(queue)
queue.enqueue("E")
queue.enqueue("F")
queue.enqueue("G")
queue.enqueue("H")
queue.enqueue("I")
queue.enqueue("J")
print(queue)
queue.dequeue()
print(queue)
for i in queue:
    print("Element:", i)
print("Peek:", queue.peek())
while not queue.is_empty():
    queue.dequeue()
print(queue)
