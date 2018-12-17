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
            if other in (None,False):return True
            return self.weight<other if type(other) in (int,float) else self.weight<other.weight
        def __gt__(self,other):
            if other in (None,False):return False
            return self.weight>other if type(other) in (int,float) else self.weight>other.weight
        def __le__(self,other):
            if other in (None,False):return True
            return self.weight<=other if type(other) in (int,float) else self.weight<=other.weight
        def __ge__(self,other):
            if other in (None,False):return False
            return self.weight>=other if type(other) in (int,float) else self.weight>=other.weight
        def __eq__(self,other):
            if other in (None,False):return False
            return self.a==other or self.b==other if type(other) is int else self.weight==other.weight
        def __ne__(self,other):
            if other in (None,False):return True
            return self.a!=other and self.b!=other if type(other) is int else self.weight!=other.weight

    #带权稀疏图的构造函数
    def __init__(self,p,directed = False):
        if p < 0 :raise Exception('error p<0')
        self.directed = directed                #False  默认为无向图
        self.p = p                              #点
        self.e = 0                              #边
        self.g = [ list() for i in range(p) ]   #保存图的邻接表
    #获得点的个数
    def P(self):
        return self.p
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
                if not self.directed:
                    self.g[e].append(edge)
                self.e+=1

    def show(self):
        for i in range(len(self.g)):
            print(i,end=" = ")
            for j in self.g[i]:
                print('{a:%r,b:%r,w:%r}'%(j.A(),j.B(),j.W()),end = ', ')
            print()



class DijkstraSP:
    def __init__(self,G,s):
        self.G = G   #图
        self.s = s   #起始点
        self.imh = indexMinHeap([ None for i in range(G.P())])   #辅助用最小堆
        self.edges = [None for i in range(G.P())]                 #记录
        self.distTo = [False for i in range(G.P())]                #记录到i 点最短路径权值,使用 False 标记未未到达过的节点，None标记已经连接了的点
        self.sp = list()                                          #记录结果
        #开始生成树
        p = s   #将要访问的点
        self.distTo[p] = 0   #初始权值为0
        for i in G.getEdge(p):  #访问 p 点的所有边
            otherP = i.other(p)   #获取i 边的另一个节点
            self.distTo[otherP] = i.W()  #将到otherP的权值记录到distTo
            self.imh.set(otherP,i.W())  #在最小堆中加入权值
            self.edges[otherP] = i   #保存边
        self.imh.set(p,None)    # p 点已经访问过了
        while len(self.sp) +1 < G.P():
            p = self.imh.extractMinIndex()   #获得当前权值最小的点
            self.sp.append(self.edges[p])  #添加到最短路径中
            for i in G.getEdge(p):  #访问p点的所有边
                otherP = i.other(p) #边的另一个节点
                ow = self.distTo[otherP]#获得当前到达这个节点路径的总权值
                nw = self.distTo[p]+i.W()
                if ow == False or nw<ow:   # 如果otherP没有到达过（ow == Flase）或者 新路径权值比旧路径小(nw<ow)
                    self.imh.set(otherP,nw)     #在最小堆中加入这个新路径
                    self.edges[otherP] = i      #加入联通这个路径的边
                    self.distTo[otherP] = nw    #到达otherP这点的权值为nw



