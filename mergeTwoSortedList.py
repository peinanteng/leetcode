# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        
        while l1 or l2:
            if not l1:
                cur.next = l2
                break
            if not l2:
                cur.next = l1
                break
            if l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
                cur = cur.next
        return dummy.next
        