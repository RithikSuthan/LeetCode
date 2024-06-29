class Solution:
    from collections import defaultdict,deque
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        ans=[]
        def traversal(val):
            queue=deque()
            queue.append(val)
            visited=set()
            while(queue):
                curr=queue.popleft()
                visited.add(curr)
                for ele in graph[curr]:
                    if ele not in visited and ele not in queue:
                        if ele not in graph[val]:
                            graph[val].append(ele)
                        queue.append(ele)
            graph[val].sort(key=lambda x:x)
            return graph[val]
        for i,j in edges:
            graph[j].append(i)
        print(graph)
        for i in range(n):
            if i in graph:
                ans.append(traversal(i))
            else:
                ans.append([])
        # print(graph)
        return ans