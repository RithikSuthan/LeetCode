from collections import deque
class TrieNode():
    childrens={}
    flag=False
    def __init__(self):
        self.childrens={}
        self.flag=False
                
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()        

    def addWord(self, word: str) -> None:
        curr=self.root
        for i in word:
            if i not in curr.childrens:
                curr.childrens[i]=TrieNode()
            curr=curr.childrens[i]
        curr.flag=True
    def helper(self,curr,word,ind):
        for i in range(ind,len(word)):
            if word[i]==".":
                for j in curr.childrens:
                    if self.helper(curr.childrens[j],word,i+1):
                        return True
                return False
            elif word[i] not in curr.childrens:
                return False
            curr=curr.childrens[word[i]]
        if curr.flag==True:
            return True
        return False


    def search(self, word: str) -> bool:
        curr=self.root
        for i in range(len(word)):
            if word[i]==".":
                for j in curr.childrens:
                    if self.helper(curr.childrens[j],word,i+1):
                        return True
                return False
            elif word[i] not in curr.childrens:
                return False
            curr=curr.childrens[word[i]]
        if curr.flag==True:
            return True
        return False
