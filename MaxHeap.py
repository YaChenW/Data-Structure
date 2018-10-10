from collections import deque


class MaxHeap:
    def __init__(self):
        self.data = deque()

    # 添加一个元素
    def add(self, e):
        self.data.append(e)
        self.shiftUp(len(self.data) - 1)

    # 查看堆中最大的元素
    def findMax(self):
        return self.data[0] if not self.isEmpty() else None

    # 取出堆中最大的元素
    def extractMax(self):
        e = self.findMax()
        self.data[0], self.data[self.getSize() - 1] = self.data[self.getSize() - 1], self.data[0]
        self.data.pop()
        self.shiftDown(0)
        return e

    # 元素下浮
    def shiftDown(self, index):
        if index < 0: return
        # 左孩子下标
        left = self.leftChild(index)
        # 右孩子下标
        right = self.rightChild(index)
        # 左孩子不存在则返回
        if left > len(self.data) - 1: return
        # 判断右边孩子是否存在
        maxIndex = right if right < len(self.data) - 1 and self.data[left] < self.data[right] else left
        if self.data[maxIndex] > self.data[index]:
            self.data[maxIndex], self.data[index] = self.data[index], self.data[maxIndex]
            self.shiftDown(maxIndex)

    # 元素上浮
    def shiftUp(self, index):
        while index > 0 and self.data[index] > self.data[self.parent(index)]:
            parent = self.parent(index)
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent

    # 获得父节点索引
    def parent(self, index):
        return (index - 1) // 2 if index > 0 else None

    # 获得左孩子节点的索引
    def leftChild(self, index):
        return index * 2 + 1 if index >= 0 else None

    # 获得右孩子节点的索引
    def rightChild(self, index):
        return index * 2 + 2 if index >= 0 else None

    # 获得元素个数
    def getSize(self):
        return len(self.data)

    # 是否为空
    def isEmpty(self):
        return self.getSize() == 0;
