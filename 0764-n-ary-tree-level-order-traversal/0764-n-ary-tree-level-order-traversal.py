"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        max_height=0
        main_root=root
        def height1(root,height):
            nonlocal max_height,main_root
            max_height=max(max_height,height)
            height+=1
            if root is None:
                return 0
            for child in root.children:
                height1(child,height)
                if root==main_root:
                    height=1
            return max_height+1
        def current_level(root,level,ls):
            if level==0 or not root:
                return 
            elif level==1:
                ls.append(root.val)
            else:
                for child in root.children:
                    current_level(child,level-1,ls)
            return ls
        ls=[]
        def level_Order_Traversal(root):
            nonlocal ls
            h=height1(root,0)
            # print(h)
            for i in range(1,h+1,1):
                ls.append( current_level(root,i,[]) )
        level_Order_Traversal(root)
        return ls