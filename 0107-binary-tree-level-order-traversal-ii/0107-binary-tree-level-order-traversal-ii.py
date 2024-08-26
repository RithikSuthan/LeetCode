# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def height(root):
            if root is None:
                return 0
            lheight=height(root.left)
            rheight=height(root.right)
            if lheight>rheight:
                return lheight+1
            return rheight+1
        def current_level(root,level,ls):
            # print(ls)
            if level==0 or not root:
                return 
            elif level==1:
                ls.append(root.val)
            else:
                current_level(root.left,level-1,ls)
                current_level(root.right,level-1,ls)
            return ls
        ls=[]
        def level_Order_Traversal(root):
            nonlocal ls
            h=height(root)
            for i in range(1,h+1,1):
                ls.append( current_level(root,i,[]) )
                # print()
        level_Order_Traversal(root)
        return ls[::-1]