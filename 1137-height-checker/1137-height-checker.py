class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ls=sorted(heights,key=lambda x:x)
        print(ls)
        cou=0
        for i in range(len(heights)):
            if heights[i]!=ls[i]:
                cou=cou+1
        return cou