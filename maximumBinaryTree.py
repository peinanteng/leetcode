# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, A):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(A) == 0:
            return None
        max_i, maxVal = 0, A[0]
        for i in range(1, len(A)):
            if A[i] > maxVal:
                max_i, maxVal = i, A[i]
        root = TreeNode(maxVal)
        root.left = self.constructMaximumBinaryTree(A[:max_i])
        root.right = self.constructMaximumBinaryTree(A[max_i + 1:])
        return root
