class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1==sentence2:
            return True
        ls=sentence1.split(" ")
        ls1=sentence2.split(" ")
        if len(ls1)<len(ls):
            start=0
            start1=0
            flag=False
            while(start<len(ls) and start1<len(ls1) and not flag):
                while (start<len(ls) and start1<len(ls1) and ls[start]==ls1[start1]):
                    start+=1
                    start1+=1
                # print(ls," Before  ",ls1)
                # while(not flag and start<len(ls) and ls[start] not in ls1):
                while(not flag and start<len(ls) and ls1.count(ls[start]) < ls.count(ls[start])):
                    ls1.insert(start,ls[start])
                    start+=1
                flag=True
                # print(ls," ",ls1)
            if ls1==ls:
                return True
        elif len(ls)<len(ls1):
            start=0
            start1=0
            flag=False
            while(start<len(ls) and start1<len(ls1) and not flag):
                while (start<len(ls) and start1<len(ls1) and ls[start]==ls1[start1]):
                    start+=1
                    start1+=1
                # print(ls," Before  ",ls1)
                while(not flag and start1<len(ls1) and ls.count(ls1[start1]) < ls1.count(ls1[start1])):
                    ls.insert(start1,ls1[start1])
                    start1+=1
                flag=True
                # print(ls," ",ls1)
            if ls1==ls:
                return True
        return False
