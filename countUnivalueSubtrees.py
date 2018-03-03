# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.helper(root)
        return self.ans
    
    def helper(self, root):
        if not root:
            return None
        leftValue = self.helper(root.left)
        rightValue = self.helper(root.right)
        if leftValue == rightValue == None \
        or leftValue == rightValue == root.val \
        or (leftValue == None and rightValue == root.val) \
        or (rightValue == None and leftValue == root.val):
            self.ans += 1
            return root.val
        return 2 ** 31 + 1
