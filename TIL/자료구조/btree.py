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

class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self)
    def __str__(self):
        return f"{self.elem}"

class BTreeBuilder:
    @staticmethod
    def build(sexpr):
        stack=Stack(len(sexpr))
        for token in sexpr:
            if token==")":
                r=stack.peek()
                stack.pop()
                l=stack.peek()
                stack.pop()
                if l=="(":
                    root=r
                    break
                stack.pop()
                stack.peek().left_child=l
                stack.peek().right_child=r
            elif token=="(":
                stack.push(token)
            else:
                stack.push(TreeNode(token))
        return root
             
class BTree:
    def __init__(self,root):
        self.root=root
    def traverse_inorder(self):
        ret=[]
        def inorder_recursive(root):
            if root is None:
                return
            inorder_recursive(root.left_child)
            ret.append(root)
            inorder_recursive(root.right_child)
        inorder_recursive(self.root)
        return ret
    def traverse_inorder_iterative(self):
        ret=[]
        root=self.root
        stack=Stack()
        
        while not stack.is_empty() or root is not None:
            while root is not None:
                stack.push(root)
                root=root.left_child
            node=stack.peek()
            stack.pop()
            ret.append(node)

            root=node.right_child
        return ret
    def traverse_levelorder(self):
        root=self.root
        ret=[]
        def level(root):
            if root is None:
                return 0
            else:
                rlv=level(root.right_child)
                llv=level(root.left_child)
                if rlv>llv:
                    return rlv+1
                else:
                    return llv+1

        max_=level(self.root)

        def levelorder_recursive(root,level):
            if root is not None:
                if level==1:
                    ret.append(root)
                else:
                    levelorder_recursive(root.left_child,level-1)
                    levelorder_recursive(root.right_child,level-1)
            else:
                return
        for i in range(max_):
            levelorder_recursive(root,i+1)
        return ret

    def traverse_levelorder_iterative(self):
        ret=[]
        root=self.root
        queue=Queue()
        queue.enqueue(root)
        while not queue.is_empty():
            root=queue.peek()
            ret.append(root)
            queue.dequeue()
            if root is not None:
                if root.left_child is not None:
                    queue.enqueue(root.left_child)
                if root.right_child is not None:
                    queue.enqueue(root.right_child)
        return ret


if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = BTree(root)
    actions = tree.traverse_inorder()
    print(actions)
    actions = tree.traverse_levelorder()
    print(actions)
    actions = tree.traverse_levelorder_iterative()
    print(actions)