class Solution:
    from collections import OrderedDict
    def longestPalindrome(self, s: str) -> int:
        if len(s)==1:
            return 1
        dict1=OrderedDict()
        result=0
        odd=[]
        even=[]
        for i in set(s):
            dict1[i]=s.count(i)
        print(dict1)
        for i in dict1:
            if dict1[i]%2==0:
                even.append(i)
            else:
                odd.append(i)
        if len(even)>0:
            for i in even:
                result=result+dict1[i]
        if len(odd)==1:
            result=result+dict1[odd[-1]]
        elif len(odd)>1:
            for i in range(len(odd)):
                if i==0:
                    result=result+dict1[odd[i]]
                else:
                    result=result+dict1[odd[i]]-1
        return result