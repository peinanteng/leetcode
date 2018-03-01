# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        preNode, slow, fast = None, head, head
        while fast and fast.next:
            preNode = slow
            slow = slow.next
            fast = fast.next.next
        if preNode:
            preNode.next = None

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        if slow != head:
            dummy1.next = head
        if slow.next:
            dummy2.next = slow.next
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(dummy1.next)
        root.right = self.sortedListToBST(dummy2.next)
        return root
       
