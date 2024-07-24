class Solution:
    import math
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        sum1=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                sum1+=i
                if i!=1:
                    sum1+=num//i
            print(i,sum1)
        if num==sum1:
            return True
        return False