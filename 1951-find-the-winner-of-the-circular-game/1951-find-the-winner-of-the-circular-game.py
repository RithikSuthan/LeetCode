class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ls=[i for i in range(1,n+1)]
        index=0
        while(len(ls)>1):
            index=(index+k-1)%len(ls)
            ls.pop(index)
        return ls[0]