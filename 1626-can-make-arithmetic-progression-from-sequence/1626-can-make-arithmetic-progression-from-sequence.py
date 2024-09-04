class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        pos_diff=arr[1]-arr[0]
        neg_diff=arr[0]-arr[1]
        forward=True
        backward=True
        for i in range(0,len(arr)-1):
            if not forward:
                break
            if arr[i+1]-arr[i]!=pos_diff:
                forward=False
        if forward:
            return True
        # for i in range(len(arr)-1,0,-1):
        #     if not backward:
        #         break
        #     if arr[i]-arr[i-1]!=neg_diff:
        #         backward=False
        # if backward:
        #     return True
        return False
        