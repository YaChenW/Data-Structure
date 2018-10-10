#线段树
class SegmentTree:
    def __init__(self,arr):
        self.data = arr
        self.tree = [ None for i in range(len(arr)*4)]
        self.buildSegmentTree(0,0,len(self.data)-1)
    
    def buildSegmentTree(self,index,l,r):
        if l==r:
            self.tree[index] = self.data[l]
            return
        mid = l+(r-l)//2
        leftChildIndex = self.leftChild(index)
        rightChildIndex = self.rightChild(index)
        self.buildSegmentTree(leftChildIndex,l,mid)
        self.buildSegmentTree(rightChildIndex,mid+1,r)
        self.tree[index] = self.tree[leftChildIndex] + self.tree[rightChildIndex]
        
    def leftChild(self,index):
        return index*2+1
    def rightChild(self,index):
        return index*2+2
    
    def getSize(self):
        return len(self.data)
        
    def get(self,index):
        if 0 <= index < self.getSize():
            return self.data[index]
    def query(self,queryL,queryR):
        if 0<= queryL <= queryR < self.getSize():
            return self.toQuery(0,0,self.getSize()-1,queryL,queryR)
            
    def toQuery(self,index,l,r,queryL,queryR):
        if l == queryL and r == queryR:
            return self.tree[index]
        mid = l + (r-l)//2
        leftChildIndex = self.leftChild(index)
        rightChildIndex = self.rightChild(index)
        if queryL>mid: return self.toQuery(rightChildIndex,mid+1,r,queryL,queryR)
        if queryR<=mid: return self.toQuery(leftChildIndex,l,mid,queryL,queryR)
        return self.toQuery(leftChildIndex,l,mid,queryL,mid) + self.toQuery(rightChildIndex,mid+1,r,mid+1,queryR)
    
    def set(self,index,e):
        if 0<=index<self.getSize():
            self.data[index] = e
            self.toSet( 0,0,self.getSize()-1,index )
            
    def toSet(self,treeIndex,l,r,index):
        if l==r:
            self.tree[treeIndex] = self.data[index]
            return
        leftChildIndex = self.leftChild(treeIndex)
        rightChildIndex = self.rightChild(treeIndex)
        mid = l+(r-l)//2
        self.toSet( rightChildIndex,mid+1,r,index ) if index>mid else self.toSet( leftChildIndex,l,mid,index )
        self.tree[treeIndex] = self.tree[leftChildIndex] + self.tree[rightChildIndex]
    
    

