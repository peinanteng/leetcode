# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n + 1)
    def dfs(self, start, end):
        if start == end:
            return [None]
        res = []
        for i in range(start, end):
            for l in self.dfs(start, i):
                for r in self.dfs(i + 1, end):
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    res.append(node)
        return res