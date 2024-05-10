class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        ans={}
        for i in range(len(arr)-1):
            for j in range(i,len(arr)):
                ans[arr[i]/arr[j]]=[arr[i],arr[j]]
        ans1=sorted(ans.keys())
        print(ans[ans1[k-1]])
        return ans[ans1[k-1]]