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
class Infix:
    def __init__(self, expr):
        (*self.expr,) = expr
    def translate_postfix(self):
        ops1="*","/"
        ops2="+","-"
        stack = Stack(len(self.expr))
        list_ = []
        for token in self.expr[::-1]:
            if token in ops2:
                while stack.peek() in ops1:
                    if stack.peek()==")":
                        break
                    list_.append(stack.peek())
                    stack.pop()
                stack.push(token)
            elif token in ops1:
                stack.push(token)
            elif token == ")":
                stack.push(token)
            elif token =="(":
                while stack:
                    if stack.peek()==")":
                        stack.pop()
                        break
                    list_.append(stack.peek())
                    stack.pop()
            else:
                list_.append(token)
        while stack:
            list_.append(stack.peek())
            stack.pop()

        return "".join(list_[::-1])
if __name__ == "__main__":
    expr = "3+2+4*5+3/1"
    infix = Infix(expr)
    postfix = infix.translate_postfix()
    print(postfix)