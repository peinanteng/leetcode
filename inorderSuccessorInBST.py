# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < p.val:
            return self.inorderSuccessor(root.right, p)
        if root.val == p.val:
            return self.findSmallest(root.right)
        if self.findLargest(root.left) == p:
            return root
        return self.inorderSuccessor(root.left, p)
    
    def findSmallest(self, root):
        if not root:
            return None
        node = self.findSmallest(root.left)
        return node if node else root
        
    def findLargest(self, root):
        if not root:
            return None
        node = self.findLargest(root.right)
        return node if node else root
