#索引最小堆
class indexMinHeap:
    def __init__(self,data=list()):
        self.data = data     #最小堆
        if len(data)>0:
            self.index = list(range(len(data)))
            self.reIndex = list(range(len(data)))
        else:
            self.index = list()    #保存原index下的元素在最小堆中的位置
            self.reIndex = list()  #反向索引
        self.heapify()       #堆初始化

    #获得父节点索引
    def parent(self,index):
        return (index-1)//2
    #获得左孩子索引
    def leftChilder(self,index):
        return index*2+1
    #获得右孩子索引
    def rightChilder(self,index):
        return index*2+2
    #index1，index2在堆，索引堆，反向索引堆中位置交换
    def swop(self,index1,index2):
        self.data[index1],self.data[index2] = self.data[index2],self.data[index1]
        self.index[self.reIndex[index1]],self.index[self.reIndex[index2]] = self.index[self.reIndex[index2]],self.index[self.reIndex[index1]]
        self.reIndex[index1],self.reIndex[index2] = self.reIndex[index2],self.reIndex[index1]
    #比较
    def compare(self,a,b):
        if a == None:return False
        if b == None:return True
        return a<b
    #上浮
    def shiftUp(self,index):
        if 0<index<len(self.data):
            parentIndex = self.parent(index)
            if self.compare(self.data[index],self.data[parentIndex]):
                self.swop(index,parentIndex)
                self.shiftUp(parentIndex)
    #下沉
    def shiftDown(self,index):
        if 0<=index<len(self.data):
            leftChilderIndex = self.leftChilder(index)
            rightChilderIndex = self.rightChilder(index)
            if rightChilderIndex<len(self.data) and self.compare(self.data[rightChilderIndex], self.data[leftChilderIndex]):
                if self.compare(self.data[rightChilderIndex] , self.data[index]):
                    self.swop(index,rightChilderIndex)
                    self.shiftDown(rightChilderIndex)
            elif leftChilderIndex<len(self.data):
                if self.compare(self.data[leftChilderIndex] , self.data[index]):
                    self.swop(index,leftChilderIndex)
                    self.shiftDown(leftChilderIndex)
    #获得堆中元素的个数
    def getSize(self):
        return len(self.data)
    #堆是否为空
    def isEmpty(self):
        return len(self.data) == 0
    #初始化data为堆
    def heapify(self):
        if len(self.data)>0:
            index = len(self.data)
            while index>=0:
                self.shiftDown(index)
                index-=1

    #查看最小的元素
    def finMin(self):
        return None if self.isEmpty else self.data[0]

    #查看最小元素的索引
    def findMinIndex(self):
        return None if self.isEmpty() else self.reIndex[0]
    #取出最小元素索引
    def extractMinIndex(self):
        ret = self.findMinIndex()
        self.extractMin()
        return ret

    #取出最小的元素
    def extractMin(self):
        if self.isEmpty():return
        ret = self.data[0]
        self.data[0] = None
        self.swop(0,len(self.data)-1)
        self.shiftDown(0)
        return ret

    #入堆
    def add(self,e):
        index = len(self.data)
        self.index.append(index)
        self.reIndex.append(index)
        self.data.append(e)
        self.shiftUp(index)

    #获得索引为 index 的元素
    def get(self,index):
        return None if self.isEmpty() else self.data[self.index[index]]

        #改变 索引为 index 的元素的值
    def set(self,index,v):
        oIndex = self.index[index]
        self.data[oIndex] = v
        self.shiftUp(oIndex)
        self.shiftDown(oIndex)


#带权稀疏图
#Lazy Prim
class SparseWeightedGraph:
    #边
    class edge:
        def __init__(self,a,b,w):
            if a==b:
                raise Exception('a==b')
            self.a,self.b = a,b
            self.weight = w
        #返回a节点
        def A(self):
            return self.a

        #返回b节点
        def B(self):
            return self.b
        #返回权值
        def W(self):
            return self.weight

        #给定一个节点返回另一个节点
        def other(self,x):
            return self.a if x==self.b else self.b

        #重写比较
        def __lt__(self,other):
            if other in (None,-1):return True
            return self.weight<other if type(other) in (int,float) else self.weight<other.weight
        def __gt__(self,other):
            if other in (None,-1):return False
            return self.weight>other if type(other) in (int,float) else self.weight>other.weight
        def __le__(self,other):
            if other in (None,-1):return True
            return self.weight<=other if type(other) in (int,float) else self.weight<=other.weight
        def __ge__(self,other):
            if other in (None,-1):return False
            return self.weight>=other if type(other) in (int,float) else self.weight>=other.weight
        def __eq__(self,other):
            if other in (None,-1):return False
            return self.a==other or self.b==other if type(other) is int else self.weight==other.weight
        def __ne__(self,other):
            if other in (None,-1):return True
            return self.a!=other and self.b!=other if type(other) is int else self.weight!=other.weight

    #带权稀疏图的构造函数
    def __init__(self,p):
        if p < 0 :raise Exception('error p<0')
        self.p = p                              #点
        self.e = 0                              #边
        self.g = [ list() for i in range(p) ]   #保存图的邻接表
    #获得点的个数
    def P(self):
        return self.P
    #获得边的条数
    def E(self):
        return self.e

    #根据 p 获得边
    def getEdge(self,p):
        return self.g[p] if 0<= p < self.p else None

    #添加边
    def addEdge(self,s,e,w):
        if 0<=s<self.p and 0<=e<self.p:
            if e not in self.g[s]:
                edge = self.edge(s,e,w)
                self.g[s].append(edge)
                self.g[e].append(edge)
                self.e+=1

    def show(self):
        for i in range(len(self.g)):
            print(i,end=" = ")
            for j in self.g[i]:
                print('{a:%r,b:%r,w:%r}'%(j.A(),j.B(),j.W()),end = ', ')
            print()



#最小生成树 LazyPrim
class LazyPrimMST:
    def __init__(self,groph):
        self.groph = groph      #获取图
        self.pq = indexMinHeap()#最小索引堆辅助取出最小边
        self.visited = set()    #记录访问过的节点
        self.mst = list()        #保存最小边
        self.creatMST()
    def creatMST(self):
        print('MST')
        p=0  #起始点为  p
        for i in self.groph[p]:  #访问起始点，  遍历所有边
            self.pq.add(i)
        self.visited.add(p)    #起始点已经访问过
        while len(self.mst) < len(self.groph)-1:
            edge = self.pq.extractMin()   #获取最小的横切边
            if edge.A() in self.visited and edge.B() in self.visited:continue
            self.mst.append(edge)            #保存横切边
            np = edge.other(p)             #边的另一个节点  保存到np
            for i in self.groph[np]:       #访问np点，   遍历所有边
                if i.other(np) != p:
                    self.pq.add(i)
            self.visited.add(np)           #np已经被访问过了
            p = np




#最小生成树 Prim
class PrimMST:
    def __init__(self,groph):        #获取图
        self.groph = groph
        self.mst = list()            #保存所有横切边
        self.imh = indexMinHeap([ -1 if i!=0 else None for i in range(len(groph)) ])   #辅助用最小索引堆
        p = 0    #初始点为p
        for i in self.groph[p]:
            self.imh.set(i.other(p),i)
        while len(self.mst)+1<len(self.groph):  #当所有点都被访问过则退出循环
            edge = self.imh.extractMin() #取出最小边
            self.mst.append(edge)
            p = edge.other(p)    #将要访问的点 p
            for i in self.groph[p]:   #访问p中所有点
                otherP = i.other(p)   #边的另一个点
                edge = self.imh.data[self.imh.index[otherP]]  #访问的边
                if edge == -1 or i<edge and edge != None:       #如果当前点没有访问过，  或者当前边的权值大于访问边的权值
                    self.imh.set(otherP,i)       #将访问边放进 imh

    def show(self):
        for i in self.mst:
            print('{a:%r,b:%r,w:%r}'%(i.A(),i.B(),i.W()),end = ', ')
