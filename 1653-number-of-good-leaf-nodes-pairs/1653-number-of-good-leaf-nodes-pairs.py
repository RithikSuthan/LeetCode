# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        pairs=0
        def dfs(root):
            nonlocal pairs
            if root is None:
                return []
            if not root.left and not root.right:
                return [1]
            lheight=dfs(root.left)
            rheight=dfs(root.right)

            if lheight and rheight:
                for i in lheight:
                    for j in rheight:
                        if (i+j)<=distance:
                            pairs+=1

            # print(lheight,rheight)
            all_dist=lheight+rheight
            return [d+1 for d in all_dist]

        dfs(root)
        return pairs
                
