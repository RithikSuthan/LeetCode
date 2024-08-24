class Solution:
    def minSteps(self, n: int) -> int:
        if n<=1:
            return 0
        disp=1
        copy=0
        opr=0
        while disp<n:
            if n%disp==0:
                copy=disp
                opr+=1
            opr+=1
            disp+=copy
            
        return opr