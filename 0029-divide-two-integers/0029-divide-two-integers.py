class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        val=dividend/divisor
        if val<0:
            val=ceil(val)
        else:
            val=floor(val)
        if val>2**31-1:
            return 2**31-1
        elif val<-2**31:
            return -2**31
        return val