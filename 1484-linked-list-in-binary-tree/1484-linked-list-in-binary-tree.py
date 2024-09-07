# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,head,root):
        if not head:
            return True
        if not root:
            return False
        result=False
        if head.val==root.val:
            result=self.dfs(head.next,root.left)
            result=result or self.dfs(head.next,root.right)
        return result

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        result=self.dfs(head,root)
        # print(result," ",root.val)
        result=result or self.isSubPath(head,root.left)
        result=result or self.isSubPath(head,root.right)
        return result
        
