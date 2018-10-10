#前缀树
class Trie:
    class Node:
        def __init__(self,isWord=False):
            self.isWord = isWord
            self.next = dict()
    
    def __init__(self):
        self.root = self.Node()
        self.size = 0
    #添加单词
    def add(self,word):
        if type(word) is str:
            cur = self.root
            for i in word:
                if not i in cur.next:
                    cur.next[i] = self.Node()
                cur = cur.next[i]
            if not cur.isWord:
                cur.isWord = True
                self.size+=1
    #是否包含单词
    def conatins(self,word):
        if type(word) is str:
            cur = self.root
            for i in word:
                if not i in cur.next:return False
                cur = cur.next[i]
            return cur.isWord
        return False
    def isPrefix(self,prefix):
        if type(prefix) is str:
            cur = self.root:
                for i in prefix:
                    if not i in cur.next:return False
                    cur = cur.next[i]
                return True
        return False
