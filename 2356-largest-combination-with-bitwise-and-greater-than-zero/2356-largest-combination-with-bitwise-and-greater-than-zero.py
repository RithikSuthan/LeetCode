class Solution:
    from collections import defaultdict
    def largestCombination(self, candidates: List[int]) -> int:
        def func(val):
            temp=bin(val)
            temp=temp[2::]
            while(len(temp)<24):
                temp="0"+temp
            return temp
        
        dict1=defaultdict(int)
        ls=[]
        for ele in candidates:
            ls.append(func(ele))
        print(ls)
        max1=1
        for i in range(0,24):
            for ele in ls:
                if ele[i]=="1":
                    dict1[i]+=1
                    max1=max(max1,dict1[i])
        print(dict1)
        
        return max1
