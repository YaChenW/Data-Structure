#稀疏图
class SparseGraph:

    def __init__(self,p,directed = False):
        #使用邻接表来保存图
        self.g = [ set() for i in range(p) ]
        self.p = p    #节点数
        self.e = 0   #边数
        self.directed = directed   #表示这是一个无向图还是有向图
        self.cconect = 0        #联通分量
        self.visited = [False for i in range(p)]  #点是否被访问
        self.id = [ None for i in range(p)]   #保存点所在的联通分量
        self.f = [None for i in range(p)]#进行深度遍历时，保存是从哪里来到这个点的

    #返回节点数
    def V(self):
        return p
    #返回边数
    def E(self):
        return e
    #返回联通分量数
    def C(self):
        return self.cconect

    #添加一条边
    def addEdge(self,v,w):
        if 0<=v<self.p and 0<=w<self.p:
            if w not in self.g[v]:
                self.g[v].add(w)
                self.e+=1
                if not self.directed:
                    self.g[w].add(v)

    #深度优先遍历
    def dfs(self):
        self.cconect = 0
        def dfs(self,arr):
            for i in arr:
                if not self.visited[i]:
                    self.visited[i] = True
                    self.id[i] = self.cconect
                    dfs(self,self.g[i])

        for i in range(len(self.g)):
            if not self.visited[i]:
                self.visited[i] = True
                self.id[i] = self.cconect
                dfs(self,self.g[i])
                self.cconect+=1
    #返回 s点 和 w点 间是否有路径
    def hasPath(self,s,w):
        return self.id[s] == self.id[w] if 0<=s<self.p and 0<=w<self.p else False
    #返回 s 点到 w点的 路径
    def path(self,s,w):
        if not self.hasPath(s,w):return
        self.f = [ None for i in range(self.p) ]#进行深度遍历时，保存是从哪里来到这个点的
        visited = set()
        def dfs(self,p,visited):
            for i in self.g[p]:
                if i not in visited:
                    visited.add(i)
                    self.f[i] = p
                    dfs(self,i,visited)
        visited.add(s)
        dfs(self,s,visited)
        ret = list()
        ret.append(w)
        flag = w
        while flag != s :
            ret.append(self.f[flag])
            flag = self.f[flag]
        ret.reverse()
        return ret

    #广度优先遍历求最小路径
    def bfs(self):
        self.f = [None for i in range(self.p)]#进行深度遍历时，保存是从哪里来到这个点的
        from collections import deque
        d = deque()   #要遍历的节点
        visited = set()
        for i in range(len(self.g)):
            if i in visited:continue
            visited.add(i)
            d.append(i)
            while len(d) != 0:
                node = d.popleft()
                for j in self.g[node]:
                    if j not in visited:
                        visited.add(j)
                        d.append(j)
                        self.f[j] = node
