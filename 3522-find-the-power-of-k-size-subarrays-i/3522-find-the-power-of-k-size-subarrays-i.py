class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        def is_consecutive(ls):
            for i in range(1,len(ls)):
                if ls[i]-ls[i-1]!=1:
                    return False
            return True
        def is_sorted(ls):
            temp=sorted(ls)
            if temp!=ls:
                return False
            return True
        for i in range(len(nums)-k+1):
            temp=nums[i:i+k]
            conse=is_consecutive(temp)
            sorte=is_sorted(temp)
            if(conse and sorte):
                ans.append(max(temp))
                continue
            ans.append(-1)
        return ans