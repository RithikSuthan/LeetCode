class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        l=len(s)
        max_curr=0
        while(i<l and i<=j and j<l):
            arr=[]
            for y in set(s[i:j+1]):
                arr.append(s[i:j+1].count(y))
            while(len(s[i:j+1])-max(arr)-k)>0:
                i=i+1
            max_curr=max(max_curr,len(s[i:j+1]))
            j=j+1
        # print(max_curr)
        return max_curr