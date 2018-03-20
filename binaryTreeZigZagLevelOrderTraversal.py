# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue, res = [root], []
        flag = 0
        while queue:
            newQueue, curRes = [], []
            for node in queue:
                curRes.append(node.val)
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            queue = newQueue
            if flag == 1:
                res.append(curRes[::-1])
                flag = 0
            else:
                res.append(curRes)
                flag = 1
        return res
