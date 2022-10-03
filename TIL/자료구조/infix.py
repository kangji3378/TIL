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
    OPS1 ='+', '-'
    OPS2 = '*', '/'
    def __init__(self, expr):
        (*self.expr,) = expr
    def translate_postfix(self):
        stack = Stack(len(self.expr))
        list_ = []
        check_=1
        for token in self.expr:
            if token=='(':
                stack.push(token)
            elif token in Infix.OPS2:
                while stack and stack.peek() in Infix.OPS2:
                    list_.append(stack.peek())
                    stack.pop()
                stack.push(token)
            elif token in Infix.OPS1:
                while stack:
                    if stack.peek()=="(":
                        break
                    list_.append(stack.peek())
                    stack.pop()
                stack.push(token)
            elif token==")":
                while stack:
                    pe=stack.peek()
                    if pe=="(":
                        stack.pop()
                        break
                    list_.append(pe)
                    stack.pop()
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