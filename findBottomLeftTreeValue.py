# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        ans = 0
        while queue:
            ans = queue[0].val
            newqueue = []
            for node in queue:
                if node.left:
                    newqueue.append(node.left)
                if node.right:
                    newqueue.append(node.right)
            queue = newqueue
        return ans
