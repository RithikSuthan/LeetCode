class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        str1=""
        while(n!=0):
            if len(str1)>0 and str1[-1] ==str(n%2):
                return False
            str1=str1+str(n%2)
            n=n//2
        return True

        