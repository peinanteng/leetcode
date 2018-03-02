# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[2]
        
    def helper(self, root):
        if not root:
            return [0, 0, - 2**31 - 1]
        leftVal = self.helper(root.left)
        rightVal = self.helper(root.right)
        newLeft = max(leftVal[0], leftVal[1], 0) + root.val
        newRight = max(rightVal[0], rightVal[1], 0) + root.val
        newPath = max(leftVal[2], rightVal[2], newLeft + newRight - root.val, newLeft, newRight, root.val)
        return [newLeft, newRight, newPath]
        
