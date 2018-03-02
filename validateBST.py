# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.flag = 1
        if root:
            self.helper(root)
        return self.flag == 1
    
    def helper(self, root):
        curResult = [root.val, root.val]
        if root.left:
            leftResult = self.helper(root.left)
            if root.val <= leftResult[1]:
                self.flag = 0
            curResult[0] = min(leftResult[0], root.val)
        if root.right:
            rightResult = self.helper(root.right)
            if root.val >= rightResult[0]:
                self.flag = 0
            curResult[1] = max(rightResult[1], root.val)
        return curResult
