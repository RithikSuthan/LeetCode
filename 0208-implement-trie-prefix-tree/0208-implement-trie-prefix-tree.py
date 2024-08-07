class TrieNode():
    def __init__(self):
        self.childrens={}
        self.flag=False
class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for i in word:
            if i not in curr.childrens:
                curr.childrens[i]=TrieNode()
            curr=curr.childrens[i]
        curr.flag=True
    def search(self, word: str) -> bool:
        curr=self.root
        for i in word:
            if i not in curr.childrens:
                return False
            curr=curr.childrens[i]
        if curr.flag!=True:
            return False
        return True
        
    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for i in prefix:
            if i not in curr.childrens:
                return False
            curr=curr.childrens[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)