# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict1=defaultdict(int)
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            dict1[root.val]+=1
            inorder(root.right)
        inorder(root)
        dict1=dict( sorted(dict1.items(),key=lambda x:x[1],reverse=True)  )
        # print(dict1)
        max_ele=0
        for ele in dict1:
            max_ele=dict1[ele]
            break
        # print(max_ele)
        ls=[]
        for ele in dict1:
            if dict1[ele]==max_ele:
                ls.append(ele)
            else:
                break
        return ls