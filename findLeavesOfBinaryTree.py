# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        while root:
            curPath = []
            root = self.helper(root, curPath)
            res.append(curPath)
        return res
    
    def helper(self, root, curPath):
        if not root:
            return None
        if not root.left and not root.right:
            curPath.append(root.val)
            return None
        root.left = self.helper(root.left, curPath)
        root.right = self.helper(root.right, curPath)
        return root
    
