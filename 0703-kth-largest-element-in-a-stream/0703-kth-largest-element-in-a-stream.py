class KthLargest:
    import heapq
    minHeap=[]
    k=0
    def __init__(self, k: int, nums: List[int]):
        self.minHeap=[]
        self.k=k
        for i in nums:
            self.add(i)
        
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        # print(self.minHeap)
        val=0
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)