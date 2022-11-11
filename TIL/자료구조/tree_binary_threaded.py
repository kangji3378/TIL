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
class TreeNodeThreaded:
    def __init__(self, elem=None):
        self.elem = elem
        self.left_child = self.right_child = None
        self.left_thread = self.right_thread = False
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
                stack_proc.push(TreeNodeThreaded(expr))
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
class ThreadedBinaryTree:
    """Threaded Binary Tree"""
    def __init__(self, root=None):
        self.root = root
        self.head = TreeNodeThreaded()
        self.head.left_thread = True
        self.head.right_thread = False
        self.head.left_child = self.head
        self.head.right_child = self.head
        self.__build()
    def __build(self):
        """using inorder traversal"""
        root = self.root
        actions = []
        if root is not None:
            self.head.left_child=root
            self.head.left_thread=False
            def inorder_recursive(root):
                if root is None:
                    return
                inorder_recursive(root.left_child)
                actions.append(root)
                inorder_recursive(root.right_child)
            inorder_recursive(self.root)
        for i in range(len(actions)):
            if actions[i].left_child is None:
                actions[i].left_thread=True
                if i==0:
                    actions[i].left_child=self.head
                else:
                    actions[i].left_child=actions[i-1]
            if actions[i].right_child is None:
                actions[i].right_thread=True
                if i==len(actions)-1:
                    actions[i].right_child=self.head
                else:
                    actions[i].right_child=actions[i+1]

    def find_successor(self, root):
        node = None
        if root.right_child ==root:
            while not root.left_thread:
                root=root.left_child
            node=root
        elif root==self.root:
            if root.right_child is not None:
                root=root.right_child
                while not root.left_thread:
                    root=root.left_child
            node=root
        else:
            node=root.right_child
        return node
    def traverse_inorder(self):
        root = self.find_successor(self.head)
        ret = []
        while root is not None and root is not self.head:
            ret.append(root)
            root = self.find_successor(root)
        return ret
    def traverse_preorder(self):
        ret=[]
        def find_sc(root):
            node=None
            if root.right_child ==root:
                while not root.left_thread:
                    root=root.left_child
                    ret.append(root)
                node=root
            elif root==self.root:
                if root.right_child is not None:
                    root=root.right_child
                    ret.append(root)
                    while not root.left_thread:
                        root=root.left_child
                        ret.append(root)
                node=root
            else:
                node=root.right_child
                if not root.right_thread:
                    ret.append(node)
            return node
        root = find_sc(self.head)
        while root is not None and root is not self.head:
            root = find_sc(root)
        return ret
if __name__ == "__main__":
    sexpr = "( A ( B ( D ( H I ) E ) C ( F G ) ) )".split()
    root_ = BTreeBuilder.build(sexpr)
    tree = ThreadedBinaryTree(root_)
    root = tree.root
    e = root.left_child.right_child
    print(f"{e.left_child} <{e}> {e.right_child}")
    f = root.right_child.left_child
    print(f"{f.left_child} <{f}> {f.right_child}")
    g = root.right_child.right_child
    print(f"{g.left_child} <{g}> {g.right_child}")
    h = root.left_child.left_child.left_child
    print(f"{h.left_child} <{h}> {h.right_child}")
    i = root.left_child.left_child.right_child
    print(f"{i.left_child} <{i}> {i.right_child}")
    print()
    actions = tree.traverse_inorder()
    print(actions)
    actions = tree.traverse_preorder()
    print(actions)