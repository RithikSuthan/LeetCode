class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        ls=sentence.split(" ")
        for i in range(0,len(ls)-1):
            if ls[i][-1]!=ls[i+1][0]:
                return False
        if ls[-1][-1]!=ls[0][0]:
            return False
        return True