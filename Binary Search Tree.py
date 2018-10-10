from collections import deque


# 二分搜索树,左结点比根节点小,右节点比根节点大
class BST:
    class Node:
        def __init__(self, e=None, left=None, right=None):
            self.e = e
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None
        self.size = 0

    # 添加节点
    def add(self, e, node=-1):
        if node == -1:
            self.root = self.add(e, self.root)
            return
        if node == None:
            self.size += 1
            return self.Node(e)
        if e > node.e:
            node.right = self.add(e, node.right)
        elif e < node.e:
            node.left = self.add(e, node.left)
        return node

    # 查询节点
    def contaions(self, e, node=-1):
        if node == -1:
            node = self.root
        if node == None:
            return False
        if node.e == e:
            return True
        return self.contaions(e, node.right) if e > node.e else self.contaions(e, node.left)

    # 前序遍历
    def preOrder(self, node=-1):
        if node == -1: node = self.root
        if node == None: return
        print(node.e)
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历
    def inOrder(self, node=-1):
        if node == -1: node = self.root
        if node == None: return
        self.inOrder(node.left)
        print(node.e)
        self.inOrder(node.right)

    # 后序遍历
    def postOrder(self, node=-1):
        if node == -1: node = self.root
        if node == None: return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.e)

    # 层级遍历
    def levelOrder(self):
        if self.size == 0: return
        q = deque()
        q.append(self.root)
        while len(q) > 0:
            node = q.popleft()
            print(node.e)
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)

    # 找到最小的元素
    def minimum(self, node=-1):
        if self.size == 0: return
        if node == -1: node = self.root
        if node.left == None: return node.e
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

    def maximum(self, node=-1):
        if self.size == 0: return
        if node == -1: node = self.root
        if node.right == None: return node.e
        return self.maximum(node.right)

    # 删除最大的元素
    def removeMax(self, node=-1):
        if self.size == 0: return None
        if node == -1:
            node = self.root
            ret = self.maximum(node)
            self.root = self.removeMax(node)
            return ret
        if node.right == None:
            ret = node.left
            node.left = None
            self.size -= 1
            return ret
        node.right = self.removeMax(node.right)
        return node

    # isEmpty
    def isEmpty(self):
        return self.size == 0

    # 删除元素 e
    def remove(self, e, node=-1):
        if node == -1:
            self.root = self.remove(e, self.root)
            return
        if node == None: return
        if node.e == e:
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
        if e > node.e:
            node.right = self.remove(e, node.right)
        else:
            node.left = self.remove(e, node.left)
        return node