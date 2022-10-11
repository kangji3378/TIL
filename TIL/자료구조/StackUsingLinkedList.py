class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if self is other or self.item == other.item:
            return True
        return False
    def __str__(self):
        return f"{self.item}"
class SinglyLinkedList:
    def __init__(self):
        self.head = self.next_ = None
    def __iter__(self):
        self.next_ = self.head
        return self
    def __next__(self):
        if self.next_ is None:
            raise StopIteration
        else:
            item = self.next_.item
            self.next_ = self.next_.next
            return item
    def add_head(self, node_new):
        r=self.head
        node_new.next=r
        self.head=node_new
    def add_tail(self, node_new):
        r=self.head
        if r is None:
            self.add_head(node_new)
        else:
            while r.next is not None:
                r=r.next
            r.next=node_new
    def delete_tail(self):
        if self.head.next is None:
            self.delete_head()
        else:
            cur_r = self.head
            pre_r = self.head
            while cur_r.next is not None:
                pre_r = cur_r
                cur_r = cur_r.next
            pre_r.next = None
    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next
    def insert_after(self, node, node_new):
        r=self.head
        while r is not None:
            if r==node:
                node_new.next=r.next
                r.next=node_new
                break
            r=r.next
    def insert_before(self, node, node_new):
        if self.head==node:
            self.add_head(node_new)
        else:
            cur_r=self.head
            pre_r=self.head
            while cur_r is not None:
                if cur_r==node:
                    pre_r.next=node_new
                    node_new.next=cur_r
                    break
                pre_r=cur_r
                cur_r=cur_r.next
    def __str__(self):
        return "["+", ".join(str(v) for v in self)+"]"
class Stack:
    def __init__(self):
        self.list_ = SinglyLinkedList()
    def push(self, elem):
        elem_=Node(elem)
        self.list_.add_head(elem_)
    def pop(self):
        self.list_.delete_head()
    def peek(self):
        if self.list_.head is None:
            return None
        p=self.list_.head
        return p
    def is_empty(self):
        if self.list_.head is None:
            return True
        return False
    def __iter__(self):
        p=self.list_.head
        while p.next is not None:
            yield p
            p=p.next
        yield p
    def __str__(self):
        return str(self.list_)
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack)
    print("peek:", stack.peek())
    stack.pop()
    print(stack)
    stack.push(30)
    print(stack)
    stack.push(40)
    print(stack)
    print("peek:", stack.peek())
    stack.pop()
    print(stack)
    for i in stack:
        print("Element:", i)
    print()
    print(stack)
    while not stack.is_empty():
        print("peek:", stack.peek())
        stack.pop()
        print(stack)