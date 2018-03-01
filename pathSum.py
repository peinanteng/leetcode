# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.helper(root, sum, [], 0)
    
    def helper(self, node, target, path, flag):
        if not node:
            if len(path) > 0 and sum(path) == target:
                flag = 1
            return flag == 1
        leftTruth = self.helper(node.left, target, path + [node.val], flag)
        rightTruth = self.helper(node.right, target, path + [node.val], flag)
        if not node.right and node.left:
            return leftTruth
        if not node.left and node.right:
            return rightTruth
        return  leftTruth or rightTruth
        
