# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue=deque()
        queue.append(root)
        levelSum=[]
        while queue:
            temp=0
            for _ in range(len(queue)):
                curr=queue.popleft()
                temp+=curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            levelSum.append(temp)
        levelSum.sort()
        if k>len(levelSum):
            return -1
        return levelSum[-k]