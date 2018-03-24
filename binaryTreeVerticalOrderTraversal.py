# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        i = - self.helper(root, 0)
        res = [[] for _ in range(i + 1)]
        dq = deque([[i, root]])
        while dq:
            j, node = dq.popleft()
            if j >= len(res):
                res.append([node.val])
            else:
                res[j].append(node.val)
            if node.left:
                dq.append([j - 1, node.left])
            if node.right:
                dq.append([j + 1, node.right])
            
        return res
    
    def helper(self, root, i):
        left, right = i, i
        if root.left:
            left = self.helper(root.left, i - 1)
        if root.right:
            right = self.helper(root.right, i + 1)
        return min(left, right, i)

