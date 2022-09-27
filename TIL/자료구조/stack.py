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
class Stack:
    CAPACITY = 10
    def __init__(self, capacity=CAPACITY):
        self.arr = Array(capacity)
        self.capacity = capacity
        self.top = -1
    def is_full(self):
        if self.top+1==(self.capacity):
            return True
        else:
            return False
    def is_empty(self):
        if self.top==-1:
            return True
        else:
            return False
    def push(self,elem):
        if self.is_full():
            raise Exception("stack is full")
        else:
            self.arr[self.top+1]=elem
            self.top+=1
    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        else:
            self.arr[self.top]=None
            self.top-=1
    def peek(self):
        if self.is_empty():
            return False
        else:
            return self.arr[self.top]
    def __len__(self):
        return (self.top+1)
    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.arr[pos]
            pos += 1
    def __str__(self):
        return str(self.arr)
N = 4
stack = Stack(N)
print("Length:", len(stack))
print("Is Empty:", stack.is_empty())
print("Push from 1 to", N)
for i in range(1, N + 1):
    print("Push:", i)
    stack.push(i)
    print("Stack:", stack)
    print("Peek:", stack.peek())
print("Is Empty:", stack.is_empty())
for i in stack:
    print("Element:", i)
print()
for i in range(N):
    print("Peek and Pop: ", stack.peek())
    stack.pop()
    print("Stack:", stack)
print("Length:", len(stack))
print("Is Empty:", stack.is_empty())