# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name}, {self.age}"
# k=student("kang",24)
# print(k)

# class Element:
#     def __init__(self,elem=0):
#         self.elem=elem
#     def __str__(self):
#         return f"Element: {self.elem}"
#     def __repr__(self):
#         return str(self)
#     def __add__(self,other):
#         if not isinstance(other,Element):
#             raise Exception("different type")
#         a=self.elem+other.elem
#         return Element(a)
#     def __sub__(self,other):
#         if not isinstance(other,Element):
#             raise Exception("different type")
#         a=self.elem-other.elem
#         return Element(a)

# class Elements:
#     def __init__(self,cap=10):
#         self.cap=cap
#         self.elems=[None]*cap
#     def __setitem__(self,id,item):
#         self.elems[id]=item
#     def __getitem__(self,id):
#         return self.elems[id]
#     def __str__(self):
#         return f"{self.elems}"
# elems = Elements()
# elems[0] = Element(10)
# elems[1] = Element(20)
# print(elems.elems[0])
# print(elems.elems[1])
# print(elems)

# v = None
# if not v:
#     print("Here1")
# if v is None:
#     print("Here2")
# v = 0
# if not v:
#     print("Here3")
# if v is None:
#     print("Here4")
# str_ = ""
# if not str_:
#     print("Here5")
# if str_ is None:
#     print("Here6")

# class Item:
#     def __init__(self,data):
#         self.data=data
#         self.link=None
#     def __str__(self):
#         return f"Item: {self.data}"
# def Expolore(i):
#     while i.link is not None:
#         print(f"({i})",end="->")
#         i=i.link
#     print(f"({i})")
# item0 = Item(0)
# item1 = Item(1)
# item2 = Item(2)
# item0.link=item1
# item1.link=item2
# Expolore(item0)

# class Array:
#     def __init__(self,range=10):
#         self.range=range
#         self.elems=[None]*range
#     def __getitem__(self,id):
#         return self.elems[id]
#     def __setitem__(self,id,item):
#         self.elems[id]=item
#     def __str__(self):
#         return f"{self.elems}"
#     def __len__(self):
#         return self.range
    
# arr = Array(5)
# for i in range(len(arr)):
#     arr[i]=i
# print(arr)
# index = 3
# print(f"arr[{index}] = {arr[index]}")
# for i in arr:
#     print(id(i), i)
# print(sum(arr))

class OrderedList:
    def __init__(self):
        self.elems=[]
    def is_empty(self):
        return not bool(self.elems)
    def add(self,item):
        if not self.elems:
            self.elems.append(item)
            return
        cur=0
        while cur<len(self.elems) and self.elems[cur]<=item:
            cur+=1
        self.elems.insert(cur,item)
    def remove(self,item):
        self.elems.remove(item)
    def search(self,item):
        cur=0
        while cur<len(self) and self[cur]!=item:
            cur+=1
        return False if cur>=len(self) else True
    def index(self,item):
        cur=0
        while cur<len(self) and self[cur]!=item:
            cur+=1
        return False if cur>=len(self) else cur
    def __len__(self):
        return len(self.elems)
    def __getitem__(self,index):
        return self.elems[index]
    def __str__(self):
        return f"{self.elems}"
*data, = 53, 17, 34, 23, 15, 43
print(data)
o = OrderedList()
print(o.is_empty())
for i in data:
    o.add(i)
print(o.is_empty())
print(o)
o.remove(23)
print(o)
print(o.search(43))
print(o.index(43))