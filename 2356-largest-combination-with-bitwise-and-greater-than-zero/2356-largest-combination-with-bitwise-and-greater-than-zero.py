class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        def func(val):
            temp=bin(val)
            temp=temp[2::]
            while(len(temp)<24):
                temp="0"+temp
            return temp
        ls=[]
        for ele in candidates:
            ls.append(func(ele))
        max1=1
        for i in range(0,24):
            cou=0
            for ele in ls:
                if ele[i]=="1":
                    cou+=1
                    max1=max(max1,cou)
        return max1
