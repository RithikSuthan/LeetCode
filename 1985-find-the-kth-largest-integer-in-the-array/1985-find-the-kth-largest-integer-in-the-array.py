class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num=[int(i) for i in nums]
        num.sort(reverse=True)
        print(num)
        print(num[k-1])
        return str(num[k-1])