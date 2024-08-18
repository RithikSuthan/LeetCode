class Solution(object):
    def isUgly(self, n):
        ls=[2,3,5]
        prev=-1
        while(prev!=n and n!=1):
            prev=n
            for i in ls:
                if n%i==0:
                    n=n//i
                    break
            # print(n)
        if n==1:
            return True
        return False
        