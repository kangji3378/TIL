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
class Postfix:
    OPS = "+", "-", "*", "/"
    def __init__(self, expr):
        self.expr = expr
    def evaluate(self):
        stack = Stack(len(self.expr))
        ret = 0
        for i in self.expr.split():
            if i in postfix.OPS:
                a=stack.pop()
                b=stack.pop()
                ret=self.cal(a,b,i)
            else:
                stack.push(i)

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
expr = "4 10 2 + * 7 -"
postfix = Postfix(expr)
print("Expression:", postfix)
res = postfix.evaluate()
print("Caculation:", res)