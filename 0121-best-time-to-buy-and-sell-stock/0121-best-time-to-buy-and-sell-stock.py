class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        i=0
        sell=0
        while(i<len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            if sell<prices[i]-buy:
                sell=prices[i]-buy
            i=i+1
        return sell