class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        temp=sentence.split(" ")
        t=len(searchWord)
        # print(temp)
        for i in range(len(temp)):
            if searchWord == temp[i][0:t]:
                return i+1
        return -1