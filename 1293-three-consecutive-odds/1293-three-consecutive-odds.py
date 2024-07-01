class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        end=0
        while(end<len(arr)):
            cou=0
            # print(end)
            while(end<len(arr) and arr[end]%2==1):
                end+=1
                cou+=1
            # print("cou",cou)
            if cou>=3:
                return True
            end+=1
        return False
