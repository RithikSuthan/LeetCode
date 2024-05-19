class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        dict1={
        }
        for i in range(0,len(edges)):
            if edges[i][0] not in dict1:
                dict1[edges[i][0]]=[]
            if edges[i][1] not in dict1:
                dict1[edges[i][1]]=[]
            dict1[edges[i][0]].append(edges[i][1])
            dict1[edges[i][1]].append(edges[i][0])
            if len(dict1[edges[i][0]])>1:
                return edges[i][0]
            elif len(dict1[edges[i][1]])>1:
                return edges[i][1]
            # print(dict1)
        return 0         
