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
    #上浮
    def shiftUp(self,index):
        if 0<index<len(self.data):
            parentIndex = self.parent(index)
            if self.data[parentIndex]>self.data[index]:
                self.swop(index,parentIndex)
                self.shiftUp(parentIndex)
    #下沉
    def shiftDown(self,index):
        if 0<=index<len(self.data):
            leftChilderIndex = self.leftChilder(index)
            rightChilderIndex = self.rightChilder(index)
            if rightChilderIndex<len(self.data) and self.data[rightChilderIndex] < self.data[leftChilderIndex]:
                if self.data[rightChilderIndex] < self.data[index]:
                    self.swop(index,rightChilderIndex)
                    self.shiftDown(rightChilderIndex)
            elif leftChilderIndex<len(self.data):
                if self.data[leftChilderIndex] < self.data[index]:
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
    
    #取出最小的元素
    def extractMin(self):
        if self.isEmpty():return
        ret = self.data[0]
        self.swop(0,len(self.data)-1)
        self.data.pop()
        self.index[self.reIndex[len(self.data)-1]] = None
        self.index[len(self.data)-1] = None
        self.shiftDown(0)
        return ret
    
    #入堆
    def add(self,e):
        index = len(self.data)
        self.index.append(len(index))
        self.reIndex.append(len(index))
        self.data.append(e)
        self.shiftUp(index)
        
    #获得索引为 index 的元素
    def get(self,index):
        return None if self.isEmpty() else self.data[self.index[index]] 
    
