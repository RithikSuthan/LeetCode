# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import copy
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def height(root):
            if root is None:
                return 0
            return 1+max(height(root.left),height(root.right))
        def curr_level(root,level):
            if root is None:
                return
            if level==1:
                print(root.val,end=" ")
            else:
                curr_level(root.left,level-1)
                curr_level(root.right,level-1)
        def inorder(root):
            h=height(root)
            for i in range(1,h+1):
                curr_level(root,i)
                print()

        def preorder(root):
            if root is None:
                return 
            print(root.val,end="=>")
            if root.left:
                print("If ",root.left.val)
                if root.left and root.left.right:
                    temp=root.left.right
                    while(temp.right):
                        temp=temp.right
                    print("after while ",temp.val)
                    aux=root.right
                    root.right=root.left
                    temp.right=aux
                else:
                    temp=root.right
                    root.right=root.left
                    root.right.right=temp
                root.left=None
                # print("After condition ",root.val,root.right.val,root.right.left.val)
            print("inorder")
            inorder(root)
            print()
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        