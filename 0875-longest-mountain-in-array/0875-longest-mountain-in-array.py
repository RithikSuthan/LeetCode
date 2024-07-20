class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_len=0
        for i in range(len(arr)):
            curr=arr[i]
            left=0
            right=0
            for l in range(i,0,-1):
                if arr[l-1]<arr[l]:
                    left+=1
                else:
                    break
            for r in range(i+1,len(arr)):
                if arr[r]<curr and arr[r-1]>arr[r]:
                    right+=1
                else:
                    break
            # print(curr,left,right)
            if left!=0 and right!=0:
                max_len=max(max_len,(left+right+1))
        return max_len