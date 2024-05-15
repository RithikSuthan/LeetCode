class Solution(object):
    def func(self,n,memo):
        if n==0 or n==1:
            return 1
        if n not in memo:
            memo[n]=self.func(n-1,memo)+self.func(n-2,memo)
        print(memo)
        return memo[n]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        return self.func(n,memo)
        
        