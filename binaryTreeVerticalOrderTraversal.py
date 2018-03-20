# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root:
            return []
        index = - self.helper(root, 0)
        res = [[] for _ in range(index + 1)]
        dq = deque([[index, root]])
        while dq:
            item = dq.popleft()
            i, node = item[0], item[1]
            if i >= len(res):
                res.append([node.val])
            else:
                res[i].append(node.val)
            if node.left:
                dq.append([i - 1, node.left])
            if node.right:
                dq.append([i + 1, node.right])
            
        return res
    
    def helper(self, root, index):
        left, right = index, index
        if root.left:
            left = self.helper(root.left, index - 1)
        if root.right:
            right = self.helper(root.right, index + 1)
        return min(left, right, index)
