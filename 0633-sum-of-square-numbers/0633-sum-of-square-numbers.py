class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        val=int(c**0.5)
        i=0
        j=val+1
        print(i,j)
        while(i<=j):
            sum1=i**2+j**2
            if sum1==c:
                return True
            elif sum1>c:
                j=j-1
            else:
                i=i+1
        return False