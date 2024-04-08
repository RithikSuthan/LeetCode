class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ls=[0]
        for i in range(len(gain)):
            ls.append(ls[-1]+gain[i])

        print(ls)
        return max(ls)
        