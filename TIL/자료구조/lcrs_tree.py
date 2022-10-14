# class Array:
#     CAPACITY = 10
#     def __init__(self, capacity=CAPACITY):
#         self.items = [None] * capacity
#     def __len__(self):
#         return len(self.items)
#     def __str__(self):
#         return str(self.items)
#     def __getitem__(self, index):
#         return self.items[index]
#     def __setitem__(self, index, item):
#         self.items[index] = item
# class Stack:
#     CAPACITY = 10
#     def __init__(self, capacity=CAPACITY):
#         self.arr = Array(capacity)
#         self.capacity = capacity
#         self.top = -1
#     def is_full(self):
#         if self.top+1==(self.capacity):
#             return True
#         else:
#             return False
#     def is_empty(self):
#         if self.top==-1:
#             return True
#         else:
#             return False
#     def push(self,elem):
#         if self.is_full():
#             raise Exception("stack is full")
#         else:
#             self.arr[self.top+1]=elem
#             self.top+=1
#     def pop(self):
#         if self.is_empty():
#             raise Exception("stack is empty")
#         else:
#             self.arr[self.top]=None
#             self.top-=1
#     def peek(self):
#         if self.is_empty():
#             return False
#         else:
#             return self.arr[self.top]
#     def __len__(self):
#         return (self.top+1)
#     def __iter__(self):
#         pos = 0
#         while pos < len(self):
#             yield self.arr[pos]
#             pos += 1
#     def __str__(self):
#         return str(self.arr)

# class Tree:
#     def __init__(self):
#         self.root = None
#     def build(self, sexpr):
#         stack = Stack()
#         for token in sexpr:
#             if token==")":
#                 pre_token=None
#                 while stack:
#                     if stack.peek()=="(":
#                         stack.pop()
#                         break
#                     a=stack.peek()
#                     a.right_sibling=pre_token
#                     pre_token=a
#                     stack.pop()
#                 if stack.peek():
#                     stack.peek().left_child=a
#                 else:
#                     self.root=a
#             elif token=="(":
#                 stack.push(token)
#             else:
#                 stack.push(self.TreeNode(token))
#     class TreeNode:
#         def __init__(self, elem):
#             self.elem = elem
#             self.left_child = None
#             self.right_sibling = None
#         def __repr__(self):
#             return str(self)
#         def __str__(self):
#             return f"{self.elem}"
# sexpr = "( A ( B ( E ( K L ) F ) C ( G ) D ( H ( M ) I J ) ) )"
# sexpr = sexpr.split()
# tree = Tree()
# tree.build(sexpr)
# root = tree.root
# print(root)
# b = root.left_child
# print(b)
# e = b.left_child
# print(e)
# k = e.left_child
# print(k)
# l = k.right_sibling
# print(l)
# f = e.right_sibling
# print(f)
# c = b.right_sibling
# print(c)
# d = c.right_sibling
# print(d)
# g = c.left_child
# print(g)
# h = d.left_child
# print(h)
# i = h.right_sibling
# print(i)
# j = i.right_sibling
# print(j)


class TreeNode:
        def __init__(self, elem):
            self.elem = elem
            self.left_child = None
            self.right_sibling = None
        def __repr__(self):
            return str(self)
        def __str__(self):
            return f"{self.elem}"
a=TreeNode(5)
b=a
c=TreeNode(8)
b.right_sibling=c
print(a.right_sibling)
a=5
b=a
b=8
print(a)
질문