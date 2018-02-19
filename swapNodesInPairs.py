# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = pre = ListNode(0)
        cur = head
        while cur:
            if cur.next == None:
                pre.next = ListNode(cur.val)
                pre = pre.next
                pre.next = None
                cur = cur.next
            else:
                pre.next = ListNode(cur.next.val)
                pre = pre.next
                pre.next = ListNode(cur.val)
                pre = pre.next
                cur = cur.next.next
        
        return dummy.next