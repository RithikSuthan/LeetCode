# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Codec:
    def serialize(self, root):
        queue=collections.deque([root])
        result=[]
        if root is None:
            return ""
        while queue:
            root=queue.popleft()
            if root:
                result.append(str(root.val))
                queue.append(root.left)
                queue.append(root.right)
            else:
                result.append(str(None))
        # print(result)
        while result and result[-1]=="None":
            result.pop()
        # print(result)
        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None
        
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = collections.deque([root])
        i = 1
        
        while queue and i < len(nodes):
            node = queue.popleft()
            
            if nodes[i] != "None":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1
            
            if i < len(nodes) and nodes[i] != "None":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))