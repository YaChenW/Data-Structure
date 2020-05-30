class redBlackTree:
    class Node:
        def __init__(self,key=None,val=None,color = False):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.parent = None
            self.color = color   #红色默认为False
    def __init__(self):
        self.Red = False
        self.Black = True
        self.root = None
        self.size = 0
    #获得size
    def getSize(self):
        return self.size
    #是否为空
    def isEmpty(self):
        return self.size == 0
    #获得节点颜色
    def getColor(self,node):
        return self.Red if node != None and node.color == self.Red else self.Black
    #左旋转
    def leftRotate(self,node):
        y = node.right
        node.right = y.left
        if node.right != None:
            node.right.parent = node
        y.parent = node.parent
        if node.parent != None:
            if node.parent.left == node:
                node.parent.left = y
            else:node.parent.right = y
        else:self.root = y
        y.left = node
        node.parent = y
        return y
    #右旋转
    def rightRotate(self,node):
        y = node.left
        node.left = y.right
        if node.left!=None:
            node.left.parent = node
        y.parent = node.parent
        if node.parent != None:
            if node.parent.left == node:
                node.parent.left = y
            else:node.parent.right = y
        else:self.root = y
        y.right = node
        node.parent = y
        return y 
    #添加元素
    def add(self,key,val=None):
        cur = self.root
        if cur == None:
            self.root = self.Node(key,val,self.Black)
            self.size+=1
            return
        while cur != None:
            if key == cur.key:return
            if key<cur.key:
                if cur.left == None:
                    cur.left = self.Node(key,val)
                    cur.left.parent = cur
                    self.size+=1
                    break
                else: cur = cur.left
            elif cur.right == None:
                cur.right = self.Node(key,val)
                cur.right.parent = cur
                self.size+=1
                break
            else: cur = cur.right
                
        while self.getColor(cur) == self.Red:
            parent = cur.parent
            if self.getColor(parent.left) == self.Red and self.getColor(parent.right) == self.Red:
                if self.root != parent:parent.color = self.Red
                parent.left.color,parent.right.color = self.Black,self.Black
                cur = parent.parent
            else:
                parent.color = self.Red
                if parent.left == cur:
                    #L
                    if self.getColor(cur.right) == self.Red:
                        #LR
                        self.leftRotate(cur)
                    #LL
                    parent.left.color = self.Black
                    self.rightRotate(parent)
                else:
                    #R
                    if self.getColor(cur.left) == self.Red:
                        #RL
                        self.rightRotate(cur)
                    #RR
                    parent.right.color = self.Black
                    self.leftRotate(parent)
                break
    #找到以node为根的树最小的节点
    def minimum(self,node):
        if node.left == None:return node
        return self.minimum(node.left)
    #通过key获得一个节点
    def get(self,key):
        if self.isEmpty():return
        
        def get(key,node):
            if node == None: return 
            if key == node.key:return node
            return get(key,node.left) if key < node.key else get(key,node.right)
        return get(key,self.root)
    #删除元素
    def remove(self,key):
        node = self.get(key)
        if node == None:return
        if node.left!=None and node.right!=None:
            changeNode = self.minimum(node.right)   #用来与当前node交换的node  left == None
            node.key,node.val,changeNode.key,changeNode.val = changeNode.key,changeNode.val,node.key,node.val #两个节点交换
            node = changeNode
        parent = node.parent    #记录待删除节点的父亲节点
        #待删除的节点左子树或右子树为空
        #判断删除这个节点是否会打破黑平衡
        self.blackBalance(node)
        son = None    #记录要代替node 的node的孩子节点
        if node.left == None:
            son = node.right
        else:
            son = node.left
        if son!=None:
            son.parent = parent
        if parent == None:
            self.root = son
        else:
            if parent.left == node:parent.left = son
            else:parent.right = son
        self.size-=1
        return node

    #维持黑平衡
    def blackBalance(self,node):
        if self.getColor(node) == self.Red:return   #删除红节点黑平衡不会被打破
        if self.root == node:return  #如果是根节点，树的黑高增加，黑平衡不会被打破
        parent = node.parent
        if parent.left == node:
            brother = parent.right
            if self.getColor(brother) == self.Red:
                parent.color,brother.color = self.Red,self.Black
                self.leftRotate(parent)
                brother = parent.right
            if self.getColor(brother.left) == self.getColor(brother.right) == self.Black:
                brother.color = self.Red
                if self.getColor(parent) == self.Red:
                    parent.color = self.Black
                else:self.blackBalance(parent)
            else:
                if self.getColor(brother.left) == self.Red:
                    brother.left.color = self.Black
                    self.rightRotate(brother)
                    brother = parent.right
                parent.color,brother.color = brother.color,parent.color
                brother.right.color = self.Black
                self.leftRotate(parent)
                return
        else:
            brother = parent.left
            if self.getColor(brother) == self.Red:
                parent.color,brother.color = self.Red,self.Black
                self.rightRotate(parent)
                brother = parent.left
            if self.getColor(brother.left) == self.getColor(brother.right) == self.Black:
                brother.color = self.Red
                if self.getColor(parent) == self.Red:
                    parent.color = self.Black
                else:self.blackBalance(parent)
            else:
                if self.getColor(brother.right) == self.Red:
                    brother.right.color = self.Black
                    self.leftRotate(brother)
                    brother = parent.left
                parent.color,brother.color = brother.color,parent.color
                brother.left.color = self.Black
                self.rightRotate(parent)
                return
    #获得key
    def getKey(self,node):
        return node.key if node != None else None
    #检测RBT
    def isRBT(self):
        
        def isRBT(self,node):
            if node == None: return 1
            leftBlack = isRBT(self,node.left)
            rightBlack = isRBT(self,node.right)
            if leftBlack!=False and rightBlack!=False and leftBlack - rightBlack == 0:
                return leftBlack if self.getColor(node) == self.Red else leftBlack+1
            else:return False
        return isRBT(self,self.root) != False
    #中序遍历
    def inOrder(self):
        def inOrder(node):
            if node == None:return []
            ret = list()
            ret.extend(inOrder(node.left))
            ret.append(node.key)
            ret.extend(inOrder(node.right))
            return ret
        return inOrder(self.root)
