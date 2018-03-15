# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preOrder, inOrder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preOrder) == 0:
            return None
        root = TreeNode(preOrder[0])
        i = inOrder.index(preOrder[0])
        root.left = self.buildTree(preOrder[1 : i + 1], inOrder[:i])
        root.right = self.buildTree(preOrder[i + 1:], inOrder[i + 1:])
        return root
