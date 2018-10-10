class LinkedList:
    class Node:
        def __init__(self, e=None, nextNode=None):
            self.e = e
            self.next = nextNode

    def __init__(self):
        self.dummyHead = self.Node()
        self.size = 0

    # 增
    def add(self, index, e, depth=0, cur=None):
        if (0 <= index <= self.size):
            if cur == None:
                cur = self.dummyHead
            if index == depth:
                cur.next = self.Node(e, cur.next)
                self.size += 1
            else:
                self.add(index, e, depth + 1, cur.next)

    def addFrist(self, e):
        self.add(0, e)

    def addLast(self, e):
        self.add(self.size, e)

    # 删
    def remove(self, index):
        if (0 <= index <= self.size):
            cur = self.dummyHead
            for i in range(index):
                cur = cur.next
            e = cur.next.e
            cur.next = cur.next.next
            self.size -= 1
            return e

    def removeFirst(self):
        return self.remove(0)

    def removeLast(self):
        return self.remove(self.size)

    # 改
    def set(self, index, e):
        if 0 <= index <= self.size:
            cur = self.dummyHead.next
            for i in range(index):
                cur = cur.next
            cur.e = e

    # 查
    def get(self, index):
        if 0 <= index <= self.size:
            cur = self.dummyHead.next
            for i in range(index):
                cur = cur.next
            return cur.e

    def getFirst(self):
        return self.get(0)

    def getLast(self):
        return self.get(self.size - 1)

    def toString(self):
        res = "LinkedList:"
        if self.size > 0:
            cur = self.dummyHead.next
            for i in range(self.size):
                res += str(cur.e) + "->"
                cur = cur.next
            res += "Null"
            return res

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0