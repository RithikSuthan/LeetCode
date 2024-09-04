class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        pos_diff=arr[1]-arr[0]
        forward=True
        for i in range(0,len(arr)-1):
            if not forward:
                break
            if arr[i+1]-arr[i]!=pos_diff:
                forward=False
        if forward:
            return True
        return False
        