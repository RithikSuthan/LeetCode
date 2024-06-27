class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dict1={}
        for i in range(1,len(edges)+2,1):
            dict1[i]=[]
        for i in edges:
            dict1[i[0]].append(i[1])
            dict1[i[1]].append(i[0])
        print(dict1)
        for i in dict1:
            if len(dict1[i])==len(edges):
                return i
        return -1
