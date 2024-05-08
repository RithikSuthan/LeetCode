class KthLargest:
    ans=[]
    k=0
    def __init__(self, k: int, nums: List[int]):
        self.ans=nums
        self.k=k
    def add(self, val: int) -> int:
        self.ans.append(val)
        self.ans.sort(reverse=True)
        # print(self.ans)
        if self.k<=len(self.ans):
            return self.ans[self.k-1]
        return 0
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)