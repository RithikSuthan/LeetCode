class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort(reverse=True)
            stones[0]=stones[0]-stones[1]
            stones.pop(1)
            print(stones)
        if len(stones)==0:
            return 0
        return stones[0]