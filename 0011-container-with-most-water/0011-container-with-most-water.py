class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        max_area=0
        while(i<j):
            area_cover=(j-i)*min(height[i],height[j])
            max_area=max(area_cover,max_area)
            if height[i]<=height[j]:
                i=i+1
            else:
                j=j-1
        print(max_area)
        return max_area