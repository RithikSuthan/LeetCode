class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if int(x)>=0:
            x=x[len(x)::-1]
            print("if ",x)
            x=int(x)
        else:
            x=x[len(x):0:-1]
            print("else" ,x)
            x=-int(x)
        if x>-2**31 and x<2**31-1:
            return x
        return 0           