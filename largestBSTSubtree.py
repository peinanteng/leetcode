# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = [None, 0]
        if not root:
            return self.result[1]
        self.helper(root)
        return self.result[1]
    
    def helper(self, root):
        curResult = [root, 1, root.val, root.val]
        if root.left:
            leftResult = self.helper(root.left)
            if leftResult[0] == None or leftResult[3] >= root.val:
                curResult[0] = None
                curResult[1] = 0
            else:
                curResult[2] = leftResult[2]
                curResult[1] += leftResult[1]
        if root.right:
            rightResult = self.helper(root.right)
            if rightResult[0] == None or rightResult[2] <= root.val:
                curResult[0] = None
                curResult[1] = 0
            else:
                curResult[3] = rightResult[3]
                curResult[1] += rightResult[1]
        if self.result[1] < curResult[1]:
            self.result[0] = curResult[0]
            self.result[1] = curResult[1]
        return curResult


