class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        while(numBottles>=numExchange):
            willempty=numBottles//numExchange
            numBottles=numBottles%numExchange+willempty
            ans+=willempty
        return ans