class Solution:
    from collections import defaultdict
    def partitionLabels(self, s: str) -> List[int]:
        dict1=defaultdict()
        l=len(s)
        for i in set(s):
            dict1[i]=l-s[::-1].index(i)
        # print(dict1)
        i=0
        j=1
        result=[]
        while(i<=j and j<l):
            j=dict1[s[i]]
            # print(i," ",j)
            while True:
                prev=j
                for ele in set(s[i:j]):
                    if j<dict1[ele]:
                        j=max(j,dict1[ele])
                if prev==j:
                    break
                # print(j," ",s[i:j+1]," ",ele)
            result.append(j-i)
            i=j
        return result