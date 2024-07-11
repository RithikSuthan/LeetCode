class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        val=1
        i=0
        while(val<n):
            val=3**i
            i+=1
            print(val)
        if val!=n:
            return False
        return True