class Solution:
    from collections import deque
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict1={}
        ls=prerequisites
        for i in range(numCourses):
            dict1[i]=[]
        for u,v in ls:
            dict1[v].append(u)
        print(dict1)
        visited=[0] *numCourses
        def dfs(curr):
            if visited[curr]==1:  #checks cycle
                return False
            if visited[curr]==2:
                return True
            visited[curr]=1
            for ele in dict1[curr]:
                if not dfs(ele):
                    return False
            visited[curr]=2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True