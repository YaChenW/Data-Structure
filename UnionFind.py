class UnionFind:
    def __init__(self):
        self.data = list(range(10))
        self.rank = [ 1 for i in range(10) ]
    
    def getSize(self):
        return len(self.data)
    
    #查找元素的根结点
    def find(self,p):
        if 0<=p<self.getSize():
            while p != self.data[p]:
                p = self.data[p]
            return p
    
    #p,q是否在一个集合内
    def isConnected(self,p,q):
        return self.find(p) == self.find(q)
    #并集
    def unionElement(self,p,q):
        pRoot,qRoot= self.find(p),self.find(q)
        if self.rank(pRoot) > self.rank(qRoot):
            self.data[qRoot] = pRoot 
        else:
            self.data[pRoot] = qRoot
        if self.rank(pRoot) == self.rank(qRoot): self.rank[qRoot]+=1
        
