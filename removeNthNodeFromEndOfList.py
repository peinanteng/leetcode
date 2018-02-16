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
        if head is None or n == 0:
            return head
        if n == 1 and head.next == None:
            return None
        cur = head
        curlen = 0
        while cur:
            curlen += 1
            cur = cur.next
        m = curlen - n + 1
        
        if m == 1:
            head = head.next
        pre = head
        cur = head.next
        count = 2
        while count <= m:
            if count == m:
                pre.next = cur.next
                break
            else:
                pre, cur = cur, cur.next
                count += 1
        return head
        