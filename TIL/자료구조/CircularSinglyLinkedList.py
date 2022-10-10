class Node:
    def __init__(self,item=None):
        self.item=item
        self.next=None
    def __eq__(self,other):
        if not isinstance(other,Node):
            return False
        if self is other or self.item==other.item:
            return True
        return False
    def __str__(self):
        return f"{self.item}"
class CircularSinglyLinkedList:
    def __init__(self):
        self.tail=None
    def add_head(self, node_new):
        if self.tail is None:
            node_new.next=node_new
            self.tail=node_new
        else:
            node_new.next=self.tail.next
            self.tail.next=node_new
    def add_tail(self, node_new):
        if self.tail is None:
            node_new.next=node_new
            self.tail=node_new
        else:
            node_new.next=self.tail.next
            self.tail.next=node_new
            self.tail=node_new
    def delete_tail(self):
        if self.tail is not None:
            if self.tail==self.tail.next:  
                self.tail=None
            else:
                pre_r=self.tail
                cur_r=self.tail
                while (pre_r.next!=self.tail):
                    pre_r=cur_r
                    cur_r=cur_r.next
                self.tail=pre_r
                pre_r.next=cur_r.next
    def delete_head(self):
        if self.tail is not None:
            if self.tail==self.tail.next:
                self.tail=None
            else:
                self.tail.next=self.tail.next.next
    def insert_after(self, node, node_new):
        if self.tail is not None:
            if (self.tail==self.tail.next and self.tail==node):
                node_new.next=self.tail 
                self.tail=node_new
            elif self.tail==node:
                node_new.next=self.tail.next
                self.tail.next=node_new
                self.tail=node_new
            else:
                r=self.tail.next
                while r!=self.tail:
                    if r==node:
                        node_new.next=r.next
                        r.next=node_new
                        break
                    r=r.next
    def insert_before(self, node, node_new):
        if self.tail is not None:
            if (self.tail==self.tail.next and self.tail==node):
                node_new.next=self.tail 
                self.tail.next=node_new
            elif node==self.tail.next:
                node_new.next=self.tail.next
                self.tail.next=node_new
            else:
                cur_r=self.tail.next
                pre_r=self.tail
                while cur_r!=self.tail:
                    pre_r=cur_r
                    cur_r=cur_r.next
                    if cur_r==node:
                        pre_r.next=node_new
                        node_new.next=cur_r
                        break
    def __str__(self):
        s=""
        if self.tail is None:
            return "[]"
        r=self.tail.next
        while(r!=self.tail):
            s+=str(r.item)+","
            r=r.next
        s+=str(r.item)
        return "["+s+"]"
list_ = CircularSinglyLinkedList()
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
list_.insert_after(Node(700), Node(250))
print("8", list_)
list_.insert_before(Node(700), Node(750))
print("9", list_)