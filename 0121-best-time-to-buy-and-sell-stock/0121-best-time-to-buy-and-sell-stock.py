class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        sell=0
        for i in range(1,len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            print(buy,prices[i],sell)
            if sell<prices[i]-buy:
                sell=prices[i]-buy
                
        return sell