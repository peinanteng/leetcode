# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        curNode = head
        while curNode.next:
            if curNode.next.val == curNode.val:
                nextNode = curNode.next
                curNode.next = curNode.next.next
                nextNode.next = None
            else:
                curNode = curNode.next
                
        return head
            
                
