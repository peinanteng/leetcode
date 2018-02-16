# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return head
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        m = count - n
        if m == 0:
            return head.next
        count = 1
        cur = head
        while count < m:
            cur = cur.next
            count += 1
        cur.next = cur.next.next
        return head