from collections import deque
class Stack:
    def __init__(self):
        self.date=deque()
    def push(self,e):
        self.date.append(e)
    def pop(self):
        if (len(self.date)>0):
            return self.date.pop()
        else:
            return None
    def peek(self):
        if(len(self.date)>0):
            return self.date[len(self.date)-1]
        else:
            return None
    def getSize(self):
        return len(self.date)
    def isEmpty(self):
        return len(self.date)==0

stack = Stack()
print(stack.isEmpty())
for i in range(10):
    stack.push(i)

print('stakc=',stack)
print('type(stack)=',type(stack))
print('stack.date=',stack.date)
print('stack.pop()=',stack.pop())
print('stack.date=',stack.date)
print('stack.peek()=',stack.peek())
print('stack.getSize()=',stack.getSize())
print('stack.isEmpty()=',stack.isEmpty())
