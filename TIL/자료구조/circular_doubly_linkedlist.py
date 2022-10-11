class Node:
    def __init__(self, item=None):
        self.item = item
        self.llink = self.rlink = None
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if self is other or self.item == other.item:
            return True
        return False
    def __str__(self):
        return f"{self.item}"
    def __repr__(self):
        return str(self)
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    def add_head(self, node_new):
        if self.head is None:
            node_new.rlink=node_new
            node_new.llink=node_new
            self.head=node_new
        else:
            node_new.rlink=self.head
            node_new.llink=self.head.llink
            self.head.llink.rlink=node_new
            self.head.llink=node_new
            self.head=node_new
    def add_tail(self, node_new):
        if self.head is None:
            self.add_head(node_new)
        else:
            node_new.rlink=self.head
            node_new.llink=self.head.llink
            self.head.llink.rlink=node_new
            self.head.llink=node_new
    def delete_head(self):
        if self.is_empty():
            raise Exception("list is empty.")
        if self.head==self.head.rlink:
            self.head=None
        else:
            self.head.rlink.llink=self.head.llink
            self.head.llink.rlink=self.head.rlink
            self.head=self.head.rlink
    def delete_tail(self):
        if self.is_empty():
            raise Exception("list is empty.")
        if self.head==self.head.rlink:
            self.head=None
        else:
            self.head.llink.llink.rlink=self.head
            self.head.llink=self.head.llink.llink
    def insert_after(self, node, node_new):
        if self.is_empty():
            raise Exception("list is empty.")
        if self.head==node:
            node_new.rlink=self.head.rlink
            node_new.llink=self.head
            self.head.rlink.llink=node_new
            self.head.rlink=node_new
        else:
            r=self.head.rlink
            while r!=self.head:
                if r==node:
                    node_new.rlink=r.rlink
                    node_new.llink=r
                    r.rlink.llink=node_new
                    r.rlink=node_new
                    break
                r=r.rlink
    def insert_before(self, node, node_new):
        if self.is_empty():
            raise Exception("list is empty.")
        if self.head==node:
            node_new.llink=self.head.llink
            node_new.rlink=self.head
            self.head.llink.rlink=node_new
            self.head.llink=node_new
            self.head=node_new
        else:
            r=self.head.rlink
            while r!=self.head:
                if r==node:
                    node_new.llink=r.llink
                    node_new.rlink=r
                    r.llink.rlink=node_new
                    r.llink=node_new
                    break
                r=r.rlink
    def delete(self, node):
        if self.is_empty():
            raise Exception("list is empty.")
        if self.head==node and self.head==self.head.rlink:
            self.head=None
        elif self.head==node:
            self.head.rlink.llink=self.head.llink
            self.head.llink.rlink=self.head.rlink
            self.head=self.head.rlink
        else:
            r=self.head.rlink
            while r!=self.head:
                if r==node:
                    r.rlink.llink=r.llink
                    r.llink.rlink=r.rlink
                    break
                r=r.rlink

    def __iter__(self):
        self.next_=self.head
        self.nnext=None
        return self
    def __next__(self):
        if self.nnext==self.head:
            raise StopIteration
        else:
            r=self.next_.item
            self.next_=self.next_.rlink
            self.nnext=self.next_
            return r
    def is_empty(self):
        if self.head is None:
            return True
        return False
    def __str__(self):
        return f"["+", ".join(str(v) for v in self)+"]"
if __name__ == "__main__":
    list_ = CircularDoublyLinkedList()
    list_.add_tail(Node(10))
    list_.add_tail(Node(20))
    list_.add_head(Node(30))
    print(list_)
    for i in list_:
        print("Element:", i)
    print()
    it = iter(list_)
    while True:
        try:
            i = next(it)
        except StopIteration:
            break
        print("Element:", i)
    print(list_)
    while not list_.is_empty():
        list_.delete_tail()
        print(list_)
    list_.add_tail(Node(20))
    list_.add_head(Node(30))
    print(list_)
    list_.insert_after(Node(30), Node(40))
    list_.insert_before(Node(20), Node(10))
    print(list_)
    list_.delete(Node(40))
    print(list_)
    list_.delete(Node(30))
    print(list_)
    list_.delete(Node(20))
    print(list_)