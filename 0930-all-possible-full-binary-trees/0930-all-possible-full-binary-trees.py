# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        memo={}
        if n%2==0:
            return []
        if n==1:
            return [TreeNode()]
        if n in memo:
            return memo[n]
        res=[]
        for i in range(1,n,2):
            left=self.allPossibleFBT(i)
            right=self.allPossibleFBT(n-i-1)
            for l in left:
                for r in right:
                    res.append(TreeNode(0,l,r))
        memo[n]=res
        return memo[n]