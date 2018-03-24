# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return res
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if not node:
                res.append('#')
            else:
                res.append(node.val)
                if node.left or node.right or dq:
                    dq.append(node.left)
                    dq.append(node.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        root = TreeNode(data[0])
        dq = deque([root])
        index = 0
        while dq:
            node = dq.popleft()
            left, right = index + 1, index + 2
            if left < len(data):
                index += 1
                if data[left] == '#':
                    node.left = None
                else:
                    node.left = TreeNode(data[left])
                    dq.append(node.left)
            if right < len(data):
                index += 1
                if data[right] == '#':
                    node.right = None
                else:
                    node.right = TreeNode(data[right])
                    dq.append(node.right)
        return root