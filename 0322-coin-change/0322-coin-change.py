class Solution(object):
    def coinChange(self, coins, amount):
        memo={}
        def backtrack(coins,amount):
            result=float("inf")
            if amount in memo:
                return memo[amount]
            if amount==0:
                return 0
            for i in range(0,len(coins)):
                if amount>=coins[i]:
                    res_sub=backtrack(coins,amount-coins[i])
                    if res_sub !=float("inf") and res_sub+1<result:
                        result=res_sub+1
            memo[amount]=result
            return result
        temp=backtrack(coins,amount)
        if temp==float("inf"):
            return -1
        return temp
        