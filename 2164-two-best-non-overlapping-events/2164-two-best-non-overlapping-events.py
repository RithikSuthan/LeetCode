class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ls = []
        for ele in events:
            ls.append([ele[0],1,ele[2]])
            ls.append([ele[1]+1,-1,ele[2]])
        ls.sort()
        # print(ls)
        maxSeen = 0
        maxSum = 0

        for ele in ls:
            if ele[1] == 1:
                maxSum = max(maxSum , ele[2] + maxSeen)
            else:
                maxSeen = max(maxSeen , ele[2])
        return maxSum