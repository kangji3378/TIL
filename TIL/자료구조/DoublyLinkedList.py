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
class DoublyLinkedList:
    def __init__(self):
        self.tail= None
    def add_head(self, node_new):
        if self.tail is None:
            node_new.rlink=node_new
            node_new.llink=node_new
            self.tail=node_new
        else:
            node_new.rlink=self.tail.rlink
            node_new.llink=self.tail
            self.tail.rlink=node_new
    def add_tail(self, node_new):
        if self.tail is None:
            node_new.rlink=node_new
            node_new.llink=node_new
            self.tail=node_new
        else:
            node_new.llink=self.tail
            node_new.rlink=self.tail.rlink
            self.tail.rlink=node_new
            self.tail=node_new
    def delete_tail(self):
        if self.tail is not None:
            if self.tail.rlink==self.tail:
                self.tail=None
            else:
                self.tail.rlink.llink=self.tail.llink
                self.tail.llink.rlink=self.tail.rlink
                a=self.tail.llink
                self.tail=a
                print(self.tail)
    def delete_head(self):
        if self.tail is not None:
            if self.tail.rlink==self.tail.llink:
                self.tail=None
            else:
                self.tail.rlink=self.tail.rlink.rlink
                self.tail.rlink.rlink.llink=self.tail
    def insert_after(self, node, node_new):
        if self.tail is not None:
            if self.tail.rlink==self.tail.llink and self.tail==node:
                node_new.rlink=self.tail
                node_new.llink=self.tail
                self.tail.rlink=node_new
                self.tail.llink=node_new
            elif self.tail==node:
                node_new.rlink=self.tail.rlink
                node_new.llink=self.tail
                self.tail.rlink=node_new
                self.tail=node_new
            else:
                r=self.tail.rlink
                while r!=self.tail:
                    if r==node:
                        node_new.llink=r
                        node_new.rlink=r.rlink
                        r.rlink=node_new
                        break
                    r=r.rlink
    def insert_before(self, node, node_new):
        if self.tail is not None:
            if self.tail.rlink==self.tail.llink and self.tail==node:
                node_new.llink=self.tail
                node_new.rlink=self.tail
                self.tail.rlink=node_new
                self.tail.llink=node_new
            elif self.tail==node:
                node_new.llink=self.tail.llink
                node_new.rlink=self.tail
                self.tail.llink.rlink=node_new
                self.tail.llink=node_new
            else:
                r=self.tail.rlink
                while r!=self.tail:
                    if r==node:
                        node_new.llink=r.llink
                        node_new.rlink=r
                        r.llink.rlink=node_new
                        r.llink=node_new
                        break
                    r=r.rlink
    def __str__(self):
        s=""
        if self.tail is None:
            return "[]"
        r=self.tail.rlink
        while(r!=self.tail):
            s+=str(r.item)+","
            r=r.rlink
        s+=str(r.item)
        return "["+s+"]"
list_ = DoublyLinkedList()
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
list_.add_tail(Node(700))
print("7", list_)
list_.insert_after(Node(50), Node(250))
print("8", list_)
list_.insert_before(Node(50), Node(750))
print("9", list_)
