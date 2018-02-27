# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        curNode = root
        leftNode = None
        rightNode = None
        while curNode:
            newLeft = curNode.left
            newRight = curNode.right
            curNode.left = leftNode
            curNode.right = rightNode
            
            leftNode = newRight
            rightNode = curNode
            curNode = newLeft
        return rightNode
