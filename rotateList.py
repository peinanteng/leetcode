# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        if count == k or count == 1:
            return head
        elif count < k:
            k = k % count
        target = count - k
        
        dummy = pre = ListNode(0)
        cur = head
        count = 1
        while count <= target:
            pre, cur = cur, cur.next
            count += 1
        count = 1
        endNode = cur
        while endNode and count < k:
            endNode = endNode.next
            count += 1
        pre.next = None
        dummy.next = cur
        endNode.next = head
        return dummy.next
        
        
        
