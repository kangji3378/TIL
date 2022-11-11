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
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self)
    def __str__(self):
        return f"{self.elem}"
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
class BTree:
    def __init__(self, root):
        self.root = root
    def search_dfs(self, elem):
        ret = None
        def dfs_recursive(root):
            nonlocal ret
            if root is None:
                return
            if root.elem==elem:
                ret=elem
                return    
            dfs_recursive(root.left_child)
            dfs_recursive(root.right_child)
        dfs_recursive(self.root)
        return ret
    def search_bfs(self, elem):
        ret=None
        root=self.root
        queue=Queue()
        queue.enqueue(root)
        while not queue.is_empty():
            root=queue.peek()
            queue.dequeue()
            if root is not None:
                if root.elem==elem:
                    ret=elem
                    break
                if root.left_child is not None:
                    queue.enqueue(root.left_child)
                if root.right_child is not None:
                    queue.enqueue(root.right_child)
        return ret
    def traverse_postorder(self):
        ret = []
        def postorder_recursive(root):
            if root is None:
                return
            postorder_recursive(root.left_child)
            postorder_recursive(root.right_child)
            ret.append(root)
        postorder_recursive(self.root)
        return
    def copy(self):
        def copy_recursive(root):
            if root is None:
                return
            node = TreeNode(root.elem)
            node.left_child = copy_recursive(root.left_child)
            node.right_child = copy_recursive(root.right_child)
            return node
        return BTree(copy_recursive(self.root))
    
if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = BTree(root)
    for e in sexpr:
        found = tree.search_bfs(e)
        print("target:", e, " found:", found)
