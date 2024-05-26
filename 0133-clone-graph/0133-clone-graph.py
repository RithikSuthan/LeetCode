"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dict1={}
        queue=deque()
        queue.append(node)
        if node:
            dict1[node]=Node(node.val)
            while(queue):
                curr=queue.popleft()
                for neighbour in curr.neighbors:
                    if neighbour not in dict1:
                        dict1[neighbour]=Node(neighbour.val)
                        queue.append(neighbour)
                    dict1[curr].neighbors.append(dict1[neighbour])
        if node in dict1:
            return dict1[node]
        return None
