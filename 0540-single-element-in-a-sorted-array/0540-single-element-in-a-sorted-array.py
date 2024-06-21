class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def bin_search(ele):
            left=0
            right=len(nums)
            result=float("inf")
            while(left<=right):
                mid=(left+right)//2
                if nums[mid]==ele:
                    print(mid)
                    result=min(result,mid)
                    right=mid-1
                elif nums[mid]>ele:
                    right=mid-1
                else:
                    left=mid+1
            return result
        nums.sort()
        st=sorted(set(nums))
        for ele in st:
            val=bin_search(ele)
            print("Ele",ele,"val",val)
            if val+1==len(nums) or val+1<len(nums) and nums[val+1]!=ele:
                return ele
        return -1