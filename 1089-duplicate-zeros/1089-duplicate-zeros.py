class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp=len(arr)
        i=0
        while(i<len(arr)):
            if arr[i]==0:
                arr.insert(i+1,0)
                arr.pop(-1)
                i=i+1
                # print(arr)
            i=i+1