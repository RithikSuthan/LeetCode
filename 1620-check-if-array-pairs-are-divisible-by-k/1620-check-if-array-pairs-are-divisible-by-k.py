class Solution:
    from collections import defaultdict
    def canArrange(self, arr: List[int], k: int) -> bool:
        ls=[0]*k
        for num in arr:
            ls[num%k]+=1
        for i in range(1,k):
            if ls[i]!=ls[k - i]:
                return False
        return ls[0] % 2 == 0