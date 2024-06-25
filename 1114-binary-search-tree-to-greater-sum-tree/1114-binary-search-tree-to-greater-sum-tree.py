# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import bisect
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inorder(root,ls):
            if root is None:
                return 
            inorder(root.left,ls)
            ls.append(root.val)
            inorder(root.right,ls)
            return ls
        val=inorder(root,[])
        if not val :
            return 
        val.sort(key=lambda x:x)
        print(val)
        def greaterBST(root):
            if root is None:
                return
            greaterBST(root.left)
            ind=bisect_left(val,root.val)
            # print(ind,val[ind:],sum(val[ind+1:])+root.val)
            root.val+=sum(val[ind+1:])
            greaterBST(root.right)
        greaterBST(root)
        return root