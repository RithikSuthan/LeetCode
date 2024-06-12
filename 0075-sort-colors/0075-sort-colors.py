class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def partition(nums,lb,ub):
            start=lb+1
            end=ub-1
            pivot=nums[lb]
            while(start<=end):
                while(start<=end and nums[start]<=pivot):
                    start+=1
                while(start<=end and nums[end]>pivot):
                    end-=1
                if(start<=end):
                    nums[start],nums[end]=nums[end],nums[start]
                # print(nums," ",start," ",end)
            nums[lb],nums[end]=nums[end],nums[lb]
            return end


        def quick_sort(nums,lb,ub):
            if(lb<ub):
                pivot=partition(nums,lb,ub)
                quick_sort(nums,lb,pivot)
                quick_sort(nums,pivot+1,ub)
            return nums
        nums=quick_sort(nums,0,len(nums))
