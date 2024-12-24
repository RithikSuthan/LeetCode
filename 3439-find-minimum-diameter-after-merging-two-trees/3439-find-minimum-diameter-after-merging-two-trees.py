from collections import deque
class Solution:
    def buildAl(self, edges):
        al = {} # adjacency list
        for edge in edges:
            if edge[0] not in al:
                al[edge[0]] = []
            if edge[1] not in al:
                al[edge[1]] = []
            
            al[edge[0]].append(edge[1])
            al[edge[1]].append(edge[0])
        return al
    
    def prunesUntilRoot(self, graph):
        n = len(graph)

        queue = deque() # store all leaves (nodes w/ 1 edge)
        edge_count = {}
        for node in graph.keys():
            edge_count[node] = len(graph[node])
            if edge_count[node] == 1:
                queue.append(node)

        levels = 0
        while queue: # each level, remove all leaves
            if n == 2: # 2 left means 2 centers
                return (levels + 1, (levels * 2) + 1) # (prunes, diameter)
            elif n == 1: # only the center left
                return (levels, levels * 2) # (prunes, diameter)
            
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                for neighbor in graph[cur]: # prune leaf & update neighbor's edges
                    edge_count[neighbor] -= 1
                    if edge_count[neighbor] == 1:
                        queue.append(neighbor) # neighbor is new leaf
                n -= 1
            levels += 1
        return 0, 0 # in case the tree has no edges

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        al1 = self.buildAl(edges1)
        al2 = self.buildAl(edges2)

        prunes1, diameter1 = self.prunesUntilRoot(al1)
        prunes2, diameter2 = self.prunesUntilRoot(al2)
        # max is (diameter of either tree) or (longest path from two tree centers + 1)
        return max(prunes1 + prunes2 + 1, diameter1, diameter2) 
        
        
        