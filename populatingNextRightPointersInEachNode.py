# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        queue = []
        if root:
            queue.append(root)
        while queue:
            newQueue = []
            while queue:
                node = queue.pop(0)
                if queue:
                    node.next = queue[0]
                else:
                    node.next = None
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            queue = newQueue
