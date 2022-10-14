# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name}, {self.age}"
# k=student("kang",24)
# print(k)

# class Element:
#     def __init__(self,elem=0):
#         self.elem=elem
#     def __str__(self):
#         return f"Element: {self.elem}"
#     def __repr__(self):
#         return str(self)
#     def __add__(self,other):
#         if not isinstance(other,Element):
#             raise Exception("different type")
#         a=self.elem+other.elem
#         return Element(a)
#     def __sub__(self,other):
#         if not isinstance(other,Element):
#             raise Exception("different type")
#         a=self.elem-other.elem
#         return Element(a)

# class Elements:
#     def __init__(self,cap=10):
#         self.cap=cap
#         self.elems=[None]*cap
#     def __setitem__(self,id,item):
#         self.elems[id]=item
#     def __getitem__(self,id):
#         return self.elems[id]
#     def __str__(self):
#         return f"{self.elems}"
# elems = Elements()
# elems[0] = Element(10)
# elems[1] = Element(20)
# print(elems.elems[0])
# print(elems.elems[1])
# print(elems)

# v = None
# if not v:
#     print("Here1")
# if v is None:
#     print("Here2")
# v = 0
# if not v:
#     print("Here3")
# if v is None:
#     print("Here4")
# str_ = ""
# if not str_:
#     print("Here5")
# if str_ is None:
#     print("Here6")

# class Item:
#     def __init__(self,data):
#         self.data=data
#         self.link=None
#     def __str__(self):
#         return f"Item: {self.data}"
# def Expolore(i):
#     while i.link is not None:
#         print(f"({i})",end="->")
#         i=i.link
#     print(f"({i})")
# item0 = Item(0)
# item1 = Item(1)
# item2 = Item(2)
# item0.link=item1
# item1.link=item2
# Expolore(item0)

# class Array:
#     def __init__(self,range=10):
#         self.range=range
#         self.elems=[None]*range
#     def __getitem__(self,id):
#         return self.elems[id]
#     def __setitem__(self,id,item):
#         self.elems[id]=item
#     def __str__(self):
#         return f"{self.elems}"
#     def __len__(self):
#         return self.range
    
# arr = Array(5)
# for i in range(len(arr)):
#     arr[i]=i
# print(arr)
# index = 3
# print(f"arr[{index}] = {arr[index]}")
# for i in arr:
#     print(id(i), i)
# print(sum(arr))

# class OrderedList:
#     def __init__(self):
#         self.elems=[]
#     def is_empty(self):
#         return not bool(self.elems)
#     def add(self,item):
#         if not self.elems:
#             self.elems.append(item)
#             return
#         cur=0
#         while cur<len(self.elems) and self.elems[cur]<=item:
#             cur+=1
#         self.elems.insert(cur,item)
#     def remove(self,item):
#         self.elems.remove(item)
#     def search(self,item):
#         cur=0
#         while cur<len(self) and self[cur]!=item:
#             cur+=1
#         return False if cur>=len(self) else True
#     def index(self,item):
#         cur=0
#         while cur<len(self) and self[cur]!=item:
#             cur+=1
#         return False if cur>=len(self) else cur
#     def __len__(self):
#         return len(self.elems)
#     def __getitem__(self,index):
#         return self.elems[index]
#     def __str__(self):
#         return f"{self.elems}"
# *data, = 53, 17, 34, 23, 15, 43
# print(data)
# o = OrderedList()
# print(o.is_empty())
# for i in data:
#     o.add(i)
# print(o.is_empty())
# print(o)
# o.remove(23)
# print(o)
# print(o.search(43))
# print(o.index(43))
# class Array:
#     CAPACITY=10
#     def __init__(self,capacity=CAPACITY):
#         self.items=[None]*capacity
#     def __len__(self):
#         return len(self.items)
#     def __str__(self):
#         return str(self.items)
#     def __getitem__(self,index):
#         return self.items[index]
#     def __setitem__(self,index,item):
#         self.items[index]=item
# class Stack:
#     CAPACITY=10
#     def __init__(self,capacity=CAPACITY):
#         self.arr=Array(capacity)
#         self.capacity=capacity
#         self.top=-1
#     def push(self,item):
#         self.top+=1
#         if self.top>=self.capacity:
#             raise Exception("capacity over")
#         self.arr[self.top]=item
#     def pop(self):
#         if self.top<=-1:
#             raise Exception("empty stack")
#         self.arr[self.top]=None
#         self.top-=1
#     def peek(self):
#         if self.top<=-1:
#             raise Exception("empty stack")
#         return self.arr[self.top]
#     def is_full(self):
#         if self.capacity==self.top+1:
#             return True
#         return False
#     def is_empty(self):
#         if self.top==-1:
#             return True
#         return False
#     def __len__(self):
#         return self.top+1
#     def __iter__(self):
#         pos=0
#         while pos<len(self):
#             yield self.arr[pos]
#             pos+=1
    
#     def __str__(self):
#         return str(self.arr)

# class Queue:
#     CAPACITY=10
#     def __init__(self,capacity=CAPACITY):
#         self.arr=Array(capacity)
#         self.capacity=capacity
#         self.front=self.rear=-1
#     def is_full(self):
#         if self.rear>=self.capacity-1:
#             return True
#         return False
#     def is_empty(self):
#         if self.front==self.rear:
#             return True
#         return False
#     def enqueue(self, elem):
#         if not self.is_full():
#             self.rear+=1
#             self.arr[self.rear]=elem
#     def dequeue(self):
#         if not self.is_empty():
#             self.front+=1
#             self.arr[self.front]=None
#     def peek(self):
#         if not self.is_empty:
#             return self.arr[self.rear]
#     def __len__(self):
#         return self.rear-self.front
#     def __iter__(self):
#         if self.is_empty():
#             return
#         pos=self.front
#         while pos<=self.rear:
#             yield self.arr[pos]
#             pos+=1        
#     def __str__(self):
#         return str(self.arr)

# N = 4
# queue = Queue(N)
# print(queue.is_empty())
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.dequeue()
# queue.dequeue()
# print(len(queue), queue)
# queue.enqueue(4)
# print(len(queue), queue)

# class Queue:
#     CAPACITY=10
#     def __init__(self,capacity=CAPACITY):
#         self.capacity=capacity
#         self.arr=Array(self.capacity)
#         self.front=self.rear=-1
#     def is_empty(self):
#         return self.front==-1 and self.rear==-1
#     def is_full(self):
#         return self.front==(self.rear+1)%self.capacity
#     def peek(self):
#         if self.is_empty():
#             raise Exception("queue is empty.")
#         return self.arr[self.front]
#     def __len__(self):
#         if self.is_empty():
#             return 0
#         if self.rear>self.front:
#             return self.rear-self.front+1
#         return self.capacity-self.front+self.rear+1
#     def __str__(self):
#         return str(self.arr)
#     def __iter__(self):
#         if self.is_empty():
#             return
#         for i in range(self.front,self.front+len(self)):
#             yield self.arr[i%self.capacity]
#     def enqueue(self,elem):
#         if self.is_full():
#             raise Exception("queue is full")
#         self.rear=(self.rear+1)%self.capacity
#         self.arr[self.rear]=elem
#         if self.front<0:
#             self.front=0
#     def dequeue(self):
#         if self.is_empty():
#             raise Exception("queue is empty")
#         self.arr[self.front]=None
#         if self.front==self.rear:
#             self.front=-1
#             self.rear=-1
#         else:
#             self.front=(self.front+1)%self.capacity
# N = 8
# queue = Queue(N)
# queue.enqueue("A")
# queue.enqueue("B")
# queue.enqueue("C")
# queue.enqueue("D")
# print(queue)
# print("Peek:", queue.peek())
# queue.dequeue()
# print("Peek:", queue.peek())
# queue.dequeue()
# print(queue)
# queue.enqueue("E")
# queue.enqueue("F")
# queue.enqueue("G")
# queue.enqueue("H")
# queue.enqueue("I")
# queue.enqueue("J")
# print(queue)
# queue.dequeue()
# print(queue)
# for i in queue:
#     print("Element:", i)
# print("Peek:", queue.peek())
# while not queue.is_empty():
#     queue.dequeue()
# print(queue)
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
            return False
        else:
            self.arr[self.top+1]=elem
            self.top+=1
    def pop(self):
        if self.is_empty():
            return False
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
class Postfix:
    OPS = "+", "-", "*", "/"
    def __init__(self, expr):
        self.expr = expr
    def evaluate(self):
        stack = Stack(len(self.expr))
        ret = 0
        for i in self.expr.split(" "):
            if i not in self.OPS:
                stack.push(int(i))
            else:
                a=stack.peek()
                stack.pop()
                b=stack.peek()
                stack.pop()
                an=self.cal(b,a,i)
                stack.push(int(an))
        ret=stack.peek()
        return ret
    def cal(self, tok_1, tok_2, op):
        if op == "+":
            return tok_1 + tok_2    
        if op == "-":
            return tok_1 - tok_2
        if op == "*":
            return tok_1 * tok_2
        if op == "/":
            return tok_1 / tok_2
        raise Exception("Unknown operator.")
    def __str__(self):
        return self.expr

class Infix:
    OPS1="+","-"
    OPS2="*","/"
    def __init__(self, expr):
        (*self.expr,) = expr
    def translate_postfix(self):
        stack = Stack(len(self.expr))
        list_ = []
        for token in self.expr:
            if token in self.OPS1:
                while stack:
                    a=stack.peek()
                    if a=="(":break
                    list_.append(a)
                    stack.pop()
                stack.push(token)
            elif token in self.OPS2:
                while stack and stack.peek() in self.OPS2:
                    a=stack.peek()
                    stack.pop()
                stack.push(token)
            elif token=="(":
                stack.push(token)
            elif token==")":
                while stack:
                    a=stack.peek()
                    stack.pop()
                    if a=="(":
                        break
                    list_.append(a)
            else:
                list_.append(token)
        while stack:
            list_.append(stack.peek())
            stack.pop()
        return "".join(list_)
if __name__ == "__main__":
    expr = "a*(b+c)*d"
    infix = Infix(expr)
    postfix = infix.translate_postfix()
    print(postfix)