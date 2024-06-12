# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def height(root):
            if root is None:
                return 0
            return max(height(root.left),height(root.right))+1
        def currentLevel(root,level,ls):
            if level==0 or root is None:
                return
            if level==1:
                ls.append(root.val)
            else:
                currentLevel(root.left,level-1,ls)
                currentLevel(root.right,level-1,ls)
            return ls
        h=height(root)
        result=[]
        # print(h)
        for i in range(1,h+1,1):
            result.append(currentLevel(root,i,[]))
        # print(result)
        return [ i[-1] for i in result]