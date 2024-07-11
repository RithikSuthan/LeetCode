class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ls=[1]
        while(ls[-1]*3 <=n):
            ls.append(ls[-1]*3)
        # print(ls)
        while(n>0):
            while( ls and ls[-1] >n):
                ls.pop()
            if not ls:
                break
            if ls:
                n-=ls[-1]
                ls.pop()
            # print(ls)
            if n==0:
                return True
        return False
        