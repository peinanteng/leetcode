# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        if root:
            self.helper(root, [], sum)
        return self.res
    def helper(self, node, path, target):
        if not node.left and not node.right:
            path.append(node.val)
            if sum(path) == target:
                self.res.append(path)
            return
        if node.left:
            self.helper(node.left, path + [node.val], target)
        if node.right:
            self.helper(node.right, path + [node.val], target)
