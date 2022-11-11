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
class BSTree:
    def __init__(self,root):
        self.root=root
    def traverse_preorder(self):
        ret=[]
        def preorder_recursive(root):
            if root is None:
                return
            ret.append(root)
            preorder_recursive(root.left_child)
            preorder_recursive(root.right_child)
        preorder_recursive(self.root)
        return ret
    def insert(self,elem):
        parent=None
        root=self.root
        while root is not None:
            if root.elem==elem:
                return
            parent=root
            if root.elem<elem:
                root=root.right_child
            else:
                root=root.left_child
        if parent.elem<elem:
            parent.right_child=TreeNode(elem)
        else:
            parent.left_child=TreeNode(elem)
    def delete(self,elem):
        root=self.root
        parent=None
        while root is not None:
            if root.elem==elem:
                break
            parent=root
            if root.elem>elem:
                root=root.left_child
            else:
                root=root.right_child
        if root is None:
            raise Exception("no elem")
        if root.right_child is None and root.left_child is None:
            if parent is None:
                self.root=None
            elif parent.right_child==root:
                parent.right_child=None
            else:
                parent.left_child=None
        elif root.right_child is not None and root.left_child is not None:
            tmp=root.left_child
            tmq=None
            while tmp.right_child is not None:
                tmq=tmp
                tmp=tmp.right_child
            tmp.right_child=root.right_child
            if tmq is not None:
                tmq.right_child=tmp.left_child
                tmp.left_child=root.left_child
            if parent is None:
                self.root=tmp
            elif parent.right_child==root:
                parent.right_child=tmp
            else:
                parent.left_child=tmp
        else:
            if root.right_child is None:
                if parent is None:
                    self.root=root.left_child
                elif parent.right_child==root:
                    parent.right_child=root.left_child
                else:
                    parent.left_child=root.left_child
            else:
                if parent is None:
                    self.root=root.right_child
                elif parent.right_child==root:
                    parent.right_child=root.right_child
                else:
                    parent.left_child=root.right_child
    def search_recur(self,elem):
        if self.root is None:
            raise Exception("the root is none")
        def search_recursive(root):
            if root is None:
                return None
            if root.elem==elem:
                return elem
            if root.elem>elem:
                return search_recursive(root.left_child)
            if root.elem<elem:
                return search_recursive(root.right_child)
            return None
        return search_recursive(self.root)
    def search(self,elem):
        if self.root is None:
            raise Exception("the root is none")
        p=self.root
        while p is not None and p.elem!=elem:
            if p.elem>elem:
                p=p.left_child
            else:
                p=p.right_child
        return p
if __name__ == "__main__":
    sexpr = "( 30 ( 5 ( 2 # ) 40 ) )".split()
    sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
    root = BTreeBuilder.build(sexpr)
    tree = BSTree(root)
    actions = tree.traverse_preorder()
    print(actions)
    tree.delete(40)
    tree.delete(30)
    tree.delete(2)
    actions = tree.traverse_preorder()
    print(actions)