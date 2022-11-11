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
        self.rows = len(mat)
        self.cols = len(mat[0])
        self.sparse = [
        Term(r, c, v)
        for r, row in enumerate(mat)
        for c, v in enumerate(row)
        if v != 0
        ]
        self.size = len(self.sparse)
    def __str__(self):
        return "\n".join(str(v) for v in self.sparse)
    def transpose(self):
        if self.sparse is None:
            return
        sparse= [Term() for _ in range(self.size)]
        idx = 0
        for i in range(self.cols):
            for e in self.sparse:
                if e.col != i:
                    continue
                sparse[idx].row = e.col
                sparse[idx].col = e.row
                sparse[idx].value = e.value
                idx += 1
        return MatrixSparse(
            rows=self.cols,
            cols=self.rows,
            size=self.size,
            sparse=sparse)
    def transpose_fast(self):
        rowsize=[0]*self.cols
        rowstart=[0]*self.cols
        sum=0
        new_sparse= [Term() for _ in range(self.size)]
        for i in self.sparse:
            rowsize[i.col]+=1
        for i in range(1,self.cols):
            sum+=rowsize[i-1]
            rowstart[i]=sum
        for i in self.sparse:
            idx=i.col
            new_sparse[rowstart[idx]].row=i.col
            new_sparse[rowstart[idx]].col=i.row
            new_sparse[rowstart[idx]].value=i.value
            rowstart[idx]+=1
        return MatrixSparse(
            rows=self.cols,
            cols=self.rows,
            size=self.size,
            sparse=new_sparse)
            
def transpose_mat(mat):
    rows = len(mat)
    cols = len(mat[0])
    ret_mat = [[0] * rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            ret_mat[col][row] = mat[row][col]
    return ret_mat

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
print("transpose fast >>")
mat=mat.transpose_fast()
print(mat)