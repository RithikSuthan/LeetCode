# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        def height(root):
            if root is None:
                return 0
            lheight=height(root.left)
            rheight=height(root.right)
            return max(lheight,rheight)+1
        def currentLevel(root,level,ls):
            if level==0 or root is None:
                return
            elif level==1:
                # print(root.val," ")
                ls.append(root.val)
            else:
                currentLevel(root.left,level-1,ls)
                currentLevel(root.right,level-1,ls)
            return ls
        h=height(root)
        # print(h)

        for i in range(1,h+1,1):
            result.append(currentLevel(root,i,[]))
            # print()
        return result