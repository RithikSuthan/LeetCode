class Solution:
    from collections import defaultdict
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        dict1=defaultdict(str)
        for i in range(len(mapping)):
            dict1[str(i)]=str(mapping[i])
        mappedarr=defaultdict()
        for i in range(len(nums)):
            temp=str(nums[i])
            val=""
            for ele in temp:
                val+=dict1[ele]
            mappedarr[i]=int(val)
        mappedarr=dict(sorted(mappedarr.items(),key=lambda x:x[1]))
        ans=[]
        for i in mappedarr:
            ans.append(nums[i])
        return ans
        