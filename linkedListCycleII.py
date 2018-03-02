# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, 
        flag = 1
        while fast and fast.next and flag:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                flag = 0
        if not fast or not fast.next:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head
