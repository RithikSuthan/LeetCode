class Solution:
    import itertools
    from collections import defaultdict
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        right=0
        max1=0
        dict1=defaultdict(int)
        while(right<len(fruits)):
            dict1[fruits[right]]+=1
            while( len(dict1) >2):
                dict1[fruits[left]]-=1
                if dict1[fruits[left]]==0:
                    del dict1[fruits[left]]
                left+=1
            max1=max(max1,right-left+1)
            right+=1
        return max1