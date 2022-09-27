'''
if __name__ == "__main__":  
    class Array:
        def __init__(self,cap=10):
            self.cap=cap
            self.elems=[None]*cap
        def __setitem__(self,id,elem):
            self.elems[id]=elem
        def __getitem__(self,id):
            return self.elems[id]
        def __str__(self):
            return f"{self.elems}"
        def __len__(self):
            return len(self.elems)
            

    arr=Array(5)
    for i in range(len(arr)):
        arr[i]=i
    print(arr)
    index=3
    print(f"arr[{index}]={arr[index]}")
    for i in arr:
        print(id(i),i)
    print(sum(arr))
'''
'''
class OrderedList():
    def __init__(self):
        self.elems=[]
    def add(self,item):
        if not self.elems:
            self.elems.append(item)
            return
        cur=0
        while cur<len(self)and self[cur]<=item:
            cur+=1
        self.elems.insert(cur,item)
    def remove(self,item):
       self.elems.remove(item)
    def search(self,item):
        cur=0
        while cur <len(self) and self[cur]!=item:
            cur+=1
        return False if cur >=len(self) else True
    def is_empty(self):
        return not bool(self.elems)
    def size(self):
        return len(self.elems)

    def index(self,item):
        for i in range(len(self.elems)):
            if self.elems[i]==item:
                return i
    def __getitem__(self,index):
        return self.elems[index]
    def __str__(self):
            return f"{self.elems}"
    def __len__(self):
            return len(self.elems)
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
'''
class Term:
    def __init__(self, row=0, col=0, value=0):
        self.row = row
        self.col = col
        self.value = value
    def __str__(self):
        return f"{self.row, self.col, self.value}"
    def __repr__(self):
        return str(self)
class MatrixSparse:
    def __init__(self, rows=0, cols=0, size=0, sparse = None):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.sparse = sparse

    def build_matrix_sparse(self, mat):
        self.rows=len(mat)
        self.cols=len(mat[0])
        self.sparse={
            Term(r,c,v)
            for r,row in enumerate(mat)
            for c,v in enumerate(row)
            if v!=0
        }
        self.size=len(self.sparse)
    def transpose(self):
        if self.sparse is None:
            return
        sparse =[Term() for _ in range(self.size)]
        idx=0
        for i in range(self.cols):
            for e in self.sparse:
                if e.col!=i:
                    continue
                sparse[idx].row=e.col
                sparse[idx].col=e.row
                sparse[idx].value=e.value
        return MatrixSparse(
            rows=self.cols,
            cols=self.rows,
            size=self.size,
            sparse=self.sparse
        )
data = [
[15, 0, 0, 22, 0, -15],
[0, 11, 3, 0, 0, 0],
[0, 0, 0, -6, 0, 0],
[0, 0, 0, 0, 0, 0],
[91, 0, 0, 0, 0, 0],
[0, 0, 28, 0, 0, 0],
]
print("sparse matrix >>")
mat = MatrixSparse()
mat.build_matrix_sparse(data)
print(mat)
print("transpose >>")
mat = mat.transpose()
print(mat)
def transpose_mat(mat):
    rows=len(mat)
    cols=len(mat[0])
    ret_mat=[[0]*rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            ret_mat[col][row]=mat[row][col]
    return ret_mat















