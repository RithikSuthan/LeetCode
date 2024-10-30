class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ind=arr.index(max(arr))
        if(ind==len(arr)-1 or ind==0 or len(arr)<3):
            return False
        i=0
        prev=-1
        while(i<ind):
            if(arr[i]<=prev):
                return False
            prev=arr[i]
            i+=1
        prev=arr[ind]
        i=ind+1
        while(i<len(arr)):
            if (arr[i]>=prev):
                return False
            prev=arr[i]
            i+=1
        return True