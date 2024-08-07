class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        sell=0
        sp=True
        for i in range(1,len(prices)-1):
            print(buy,prices[i],"Profit :",profit)
            if buy>prices[i]:
                buy=prices[i]
                sp=True
                sell=prices[i]-buy
            if sp and prices[i]-buy>sell and prices[i+1]-buy<=prices[i]-buy:
                sp=False
                profit+=prices[i]-buy
                sell=0
                buy=float("inf")
        if len(prices)>1 and prices[-1]-buy>prices[-2]-buy:
            profit+=prices[-1]-buy
        return profit

                