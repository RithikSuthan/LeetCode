class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        score=0
        max_i=values[0]
        for i in range(1,len(values)):
            # print(max_i)
            score=max(score,max_i+values[i]-i)
            max_i=max(max_i,values[i]+i)
        return score