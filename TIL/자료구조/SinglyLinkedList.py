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
list_ = SinglyLinkedList()
list_.add_head(Node(50))
list_.add_tail(Node(100))
list_.add_tail(Node(150))
print("1", list_)
list_.delete_head()
print("2", list_)
list_.delete_tail()
print("3", list_)
list_.delete_head()
print("4", list_)
list_.add_tail(Node(150))
list_.insert_before(Node(150), Node(999))
print("5", list_)
list_.add_head(Node(50))
list_.add_tail(Node(100))
print("6", list_)
for i in list_:
    print("Element:", i)
list_.add_tail(Node(700))
print("7", list_)
list_.insert_after(Node(50), Node(250))
print("8", list_)
list_.insert_before(Node(50), Node(750))
print("9", list_)
for i in list_:
    print("Element:", i)