# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        dq = deque([root])
        while dq:
            newQueue = deque([])
            while dq:
                node = dq.popleft()
                node.next = dq[0] if dq else None
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            dq = newQueue