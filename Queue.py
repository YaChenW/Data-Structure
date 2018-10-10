from collections import deque
class Queue:
    def __init__(self):
        self.date=deque()
    def enqueue(self,e):
        self.date.append(e)
    def dequeue(self):
        if (len(self.date)>0):
            return self.date.popleft()
        else:
            return None
    def getFront(self):
        if(len(self.date)>0):
            return self.date[0]
        else:
            return None
    def getSize(self):
        return len(self.date)
    def isEmpty(self):
        return len(self.date)==0
queue = Queue()
for i in range(10):
    queue.enqueue(i)

print('queue=',queue)
print('type(queue)=',type(queue))
print('queue.date=',queue.date)
print('queue.dequeue()=',queue.dequeue())
print('queue.date=',queue.date)
print('queue.getFront()=',queue.getFront())
print('queue.getSize()=',queue.getSize())
print('queue.isEmpty()=',queue.isEmpty())