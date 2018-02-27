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
        if not head:
            return head
        preNode = head
        while preNode.next:
            if preNode.next.val == preNode.val:
                curNode = preNode.next
                preNode.next = preNode.next.next
                curNode.next = None
            else:
                preNode = preNode.next
                
        return head
            
                
