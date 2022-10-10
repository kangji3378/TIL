class Node:
    def __init__(self, item=None):
        self.item = item
        self.rlink = self.llink = None
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if self is other or self.item == other.item:
            return True
        return False
    def __str__(self):
        return f"{self.item}"
#L R
class DoublyLinkedList:
    def __init__(self):
        self.head= None
    def add_head(self, node_new):
        if self.head is None:
            self.head=node_new
        else:
            node_new.rlink=self.head
            self.head.llink=node_new
            self.head=node_new
    def add_tail(self, node_new):
        r=self.head
        if r is None:
            self.head=node_new
        else:
            while r.rlink is not None:
                r=r.rlink
            node_new.llink=r
            r.rlink=node_new
    def delete_tail(self):
        r=self.head
        if r is not None:
            if r.rlink is None:
                self.head=None
            else:
                while r.rlink is not None:
                    r=r.rlink
                r.llink.rlink=None
    def delete_head(self):
        r=self.head
        if r is not None:
            if r.rlink is None:
                self.head=None
            else:
                r.rlink.llink=None
                self.head=r.rlink
    def insert_after(self, node, node_new):
        r=self.head
        if r is not None:
            if node==r:
                node_new.rlink=r.rlink
                node_new.llink=r
                r.rlink.llink=node_new
                r.rlink=node_new
            else:
                while r.rlink is not None:
                    if r==node:
                        node_new.rlink=r.rlink
                        node_new.llink=r
                        r.rlink.llink=node_new
                        r.rlink=node_new
                    r=r.rlink
                if r==node:
                    node_new.llink=r
                    r.rlink=node_new
    def insert_before(self, node, node_new):
        r=self.head
        if r is not None:
            if r==node:
                node_new.rlink=r
                r.llink=node_new
                self.head=node_new
            else:
                while r.rlink is not None:
                    if r==node:
                        node_new.rlink=r
                        node_new.llink=r.llink
                        r.llink.rlink=node_new
                        r.llink=node_new
                    r=r.rlink
                if r==node:
                    node_new.rlink=r
                    node_new.llink=r.llink
                    r.llink.rlink=node_new
                    r.llink=node_new
    def __str__(self):
        s=""
        if self.head is None:
            return "[]"
        r=self.head
        while r.rlink is not None:
            s+=str(r.item)+","
            r=r.rlink
        s+=str(r.item)
        return "["+s+"]"

