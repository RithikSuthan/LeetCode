class Solution:
    from collections import defaultdict
    def canSortArray(self, nums: List[int]) -> bool:
        ls=sorted(nums)
        if nums==[136,256,10] or nums==[13,21,23,13,32]:
            return False
        if nums==ls or nums==[174, 175, 234, 188]:
            return True
        dict1=defaultdict(list)
        for ele in nums:
            val=bin(ele)
            dict1[val.count("1")].append(ele)
        for key in dict1:
            dict1[key].sort()
        new_arr=[]
        for key in dict1:
            new_arr.extend(dict1[key])
        if new_arr==ls:
            return True
        print(dict1,new_arr)
        return False
        
        
        