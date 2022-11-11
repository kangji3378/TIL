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
class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.value = None # boolean value
        self.left_child = self.right_child = None
    def __repr__(self):
        return str(self)
    def __str__(self):
        return f"{self.elem}"
class BTreeBuilder:
    @staticmethod
    def build(sexpr):
        stack_proc = Stack(len(sexpr))
        stack_subtree = Stack(len(sexpr))
        root = None
        for expr in sexpr:
            if expr != ")":
                stack_proc.push(TreeNode(expr))
                continue
            while stack_proc.peek().elem != "(":
                node = stack_proc.peek()
                stack_proc.pop()
                node = node if node.elem != "#" else None
                stack_subtree.push(node)
            stack_proc.pop()  # remove "(“
            if stack_proc.is_empty():
                root = stack_subtree.peek()
                stack_subtree.pop()
            else:
                root = stack_proc.peek()
                stack_proc.pop()
            if stack_subtree.is_empty():
                continue
            root.left_child = stack_subtree.peek()
            stack_subtree.pop()
            root.right_child = stack_subtree.peek()
            stack_subtree.pop()
            stack_proc.push(root)
        if not stack_proc.is_empty():
            raise Exception("expression is wrong.")
        return root
class PropositionalTree:
    def __init__(self,root):
        self.root=root
    def calculate_propositional(self, *param):
        ret = None
        case=[]
        for i in range(len(param)):
            case.append(str(i))
        def calculate_recursive(root):
            nonlocal ret
            if root is None:
                return
            calculate_recursive(root.left_child)
            calculate_recursive(root.right_child)
            if root.elem =="NOT":
                root.value=not root.right_child.value
            elif root.elem =="AND":
                root.value= root.right_child.value and root.left_child.value
            elif root.elem=="OR":
                root.value=root.right_child.value or root.left_child.value
            elif root.elem in case:
                root.value= param[int(root.elem)]
            else:
                raise Exception ("wrong")
            ret=root
        calculate_recursive(self.root)
        return ret
if __name__ == "__main__":
    sexpr = "( NOT ( # 0 ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = PropositionalTree(root)
    prop = tree.calculate_propositional(True, False)
    print(prop.value)