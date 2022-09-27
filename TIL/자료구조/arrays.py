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
