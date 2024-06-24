class Solution:
    from collections import deque
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max1=deque()
        min1=deque()

        i=0
        max_len=0
        for j in range(len(nums)):
            while max1 and nums[max1[-1]]<=nums[j]:
                max1.pop()
            max1.append(j)

            while min1 and nums[min1[-1]]>=nums[j]:
                min1.pop()
            min1.append(j)

            while((nums[max1[0]]-nums[min1[0]])>limit):
                i+=1
                while max1[0]<i:
                    max1.popleft()
                while min1[0]<i:
                    min1.popleft()
            max_len=max(max_len,j-i+1)
        return max_len