class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        result=1
        for i in range(2,int(num**0.5)+1,1):
            # print(i)
            if num%i==0:
                result+=i
                if num//i!=i and i!=1:#avouid doble counting
                    result+=num//i
        if result==num:
            return True
        # print(result)
        return False