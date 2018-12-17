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

    #b-m最短路径
class BellManFord:
    def __init__(self,G,s):
        self.G=G
        self.s=s
        self.f=[None for i in range(G.P())]#表示从哪个点到这个点的
        self.distTo = [None for i in range(G.P())]    #表示s 点 到i 点的权值
        self.f[s] = s    #初始化s
        self.distTo[s] = 0  #初始化s的权
        for times in range(G.P()-1):
            #最多运行 p 总数 -1次  松弛操作
            flag = True     #记录遍历一次所有边，如果没有进行松弛操作则为True，跳出循环
            for p in range(G.P()):
                if self.f[p] == None:continue
                for edge in G.getEdge(p):   #遍历p点的所有相邻边
                    otherP = edge.other(p)  #otherP为p的一个邻点
                    nw = self.distTo[p] + edge.W()  #s点进过p到达otherP的路径的权值
                    #如果这个点还没到达过，或者经过p后到达otherP的路径权值更小
                    if self.f[otherP] == None or self.distTo[otherP] > nw:
                        self.distTo[otherP] = nw    #设置新的从 s点到 otherP点路径的权值
                        self.f[otherP] = p
                        flag = False
            if flag:break

    #判断是否有负权环
    def detectNegativeCycle(self):
        for p in range(self.G.P()):
            if self.f[p] == None:continue
            for edge in self.G.getEdge(p):   #遍历p点的所有相邻边
                otherP = edge.other(p)  #otherP为p的一个邻点
                nw = self.distTo[p] + edge.W()  #s点进过p到达otherP的路径的权值
                #如果这个点还没到达过，或者经过p后到达otherP的路径权值更小
                if self.f[otherP] == None or self.distTo[otherP] > nw:
                    return True
        return False



