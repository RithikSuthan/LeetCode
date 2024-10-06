class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1==sentence2:
            return True
        ls=sentence1.split(" ")
        ls1=sentence2.split(" ")
        if len(ls1)<len(ls):#Sentence 1 greater than sentence 2
            start=0
            start1=0
            flag=False
            while(start<len(ls) and start1<len(ls1) and not flag):
                while (start<len(ls) and start1<len(ls1) and ls[start]==ls1[start1]):
                    start+=1
                    start1+=1
                while(not flag and start<len(ls) and ls1.count(ls[start]) < ls.count(ls[start])):
                    ls1.insert(start,ls[start])
                    start+=1
                flag=True
        elif len(ls)<len(ls1):#Sentence 2 greater than sentence 1
            start=0
            start1=0
            flag=False
            while(start<len(ls) and start1<len(ls1) and not flag):
                while (start<len(ls) and start1<len(ls1) and ls[start]==ls1[start1]):
                    start+=1
                    start1+=1
                while(not flag and start1<len(ls1) and ls.count(ls1[start1]) < ls1.count(ls1[start1])):
                    ls.insert(start1,ls1[start1])
                    start1+=1
                flag=True
        if ls1==ls:
            return True
        return False
