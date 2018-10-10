# 二分搜索树映射(字典)
class BSTMap():
    class Node:
        def __init__(self, K=None, V=None, left=None, right=None):
            self.K = K
            self.V = V
            self.left = left
            self.right = right

    def __init__(self):
        self.size = 0
        self.root = None

    # 添加元素
    def add(self, K, V, node=-1):
        if node == -1:
            self.root = self.add(K, V, self.root)
            return
        if node == None:
            self.size += 1
            return self.Node(K, V)
        if e > node.e:
            node.right = self.add(K, V, node.right)
        elif e < node.e:
            node.left = self.add(K, V, node.left)
        return node

    # 找到最小的元素
    def minimum(self, node=-1):
        if self.size == 0: return
        if node == -1: node = self.root
        if node.left == None: return node.K
        return self.minimum(node.left)

    # 删除最小的元素
    def removeMin(self, node=-1):
        if self.size == 0: return
        if node == -1:
            node = self.root
            ret = self.minimum(node)
            self.root = self.removeMin(node)
            return ret
        if node.left == None:
            ret = node.right
            node.right = None
            self.size -= 1
            return ret
        node.left = self.removeMin(node.left)
        return node

    # 删除元素 e
    def remove(self, K, node=-1):
        if node == -1:
            self.root = self.remove(K, self.root)
            return
        if node == None: return
        if node.K == K:
            if node.right == None:
                self.size -= 1
                return node.left
            if node.left == None:
                self.size -= 1
                return node.right
            ret = self.Node(self.removeMax(node.left))
            ret.left, ret.right = node.left, node.right
            node.left = node.right = None
            return ret
        if K > node.K:
            node.right = self.remove(K, node.right)
        else:
            node.left = self.remove(K, node.left)
        return node

    # 是否包含元素
    def contains(self, K, node=-1):
        if self.isEmpty(): return False
        if node == -1: node = self.root
        if node == None: return False
        if node.K == K: return True
        return self.contains(K, node.right) if K > node.K else self.contains(K, node.left)

    # 获得长度
    def getSize(self):
        return self.size

    # 是否为空
    def isEmpty(self):
        return self.size == 0

    # 通过K获得V
    def get(self, K):
        node = getNode(K)
        return node.V if node != None else None

        # 通过K修复V的值

    def setV(self, K, V):
        node = getNode(K)
        if node == None: return
        node.V = V

    # 通过K获得节点
    def getNode(self, K, node=-1):
        if node == -1: node = self.root
        if node == None: return None
        if node.K == K: return node
        return self.getNode(K, node, left) if node.K > K else self.getNode(K, node.right)

