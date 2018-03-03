# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        if root:
            self.helper(root, 0)
        return self.ans
    
    def helper(self, root, num):
        num = num * 10 + root.val
        if not root.left and not root.right:
            self.ans += num
            return
        if root.left:
            self.helper(root.left, num)
        if root.right:
            self.helper(root.right, num)
