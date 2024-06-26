# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root,ls):
            if root is None:
                return
            inorder(root.left,ls)
            ls.append(root.val)
            inorder(root.right,ls)

            return ls

        def build_tree(ls,start,end):
            mid=(start+end)//2
            if(start>=end):
                return None
            root=TreeNode(ls[mid])

            root.left=build_tree(ls,start,mid)
            root.right=build_tree(ls,mid+1,end)

            return root
        ls=inorder(root,[])
        return build_tree(ls,0,len(ls))

