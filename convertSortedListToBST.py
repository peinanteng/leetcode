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
        count = 0
        curNode = head
        while curNode:
            count += 1
            curNode = curNode.next
        target = (count) // 2
        count = 0
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        dummy1.next = head
        preNode, curNode = dummy1, head
        while count < target:
            count += 1
            preNode, curNode = curNode, curNode.next
        preNode.next = None
        if curNode.next:
            dummy2.next = curNode.next
        root = TreeNode(curNode.val)
        root.left = self.sortedListToBST(dummy1.next)
        root.right = self.sortedListToBST(dummy2.next)
        return root
            
       
