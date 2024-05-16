class Solution:
    def steps(self,cost,memo,n):
        if n==0:
            return 0
        if n not in memo:
            memo[n]=min(self.steps(cost,memo,n-1),self.steps(cost,memo,n-2))+cost[n-1]
        # print(memo)
        return memo[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={1:cost[0],2:cost[1]}
        val=min(self.steps(cost, memo, len(cost)), self.steps(cost, memo,len(cost)-1))
        # print(val)
        return val