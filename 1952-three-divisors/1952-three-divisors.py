class Solution:
    def isThree(self, n: int) -> bool:
        i=1
        cou=1
        while(i<n):
            if n%i==0:
                cou=cou+1
            if cou>3:
                return False
            i=i+1
        print(cou)
        if cou==3:
            return True
        return False 