from collections import defaultdict
class Solution:
    import bisect
    def maximumBeauty(self, items, queries):
        mydict=defaultdict(int)
        items.sort()
        max_beauty=0
        for price,beauty in items:
            max_beauty=max(max_beauty,beauty)
            mydict[price]=max_beauty
        ls=list(mydict.keys())
        ans=[]
        for item in queries:
            ind=bisect.bisect_right(ls,item)-1
            if ind>=0:
                ans.append(mydict[ls[ind]])
            else:
                ans.append(0)
        return ans
