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
        dummy = preNode = ListNode(0)
        while l1 or l2:
            if not l1:
                preNode.next = l2
                break
            if not l2:
                preNode.next = l1
                break
            if l1.val <= l2.val:
                curNode = l1
                nextNode = curNode.next
                curNode.next = None
                preNode.next = curNode
                preNode = preNode.next
                l1 = nextNode
            else:
                curNode = l2
                nextNode = curNode.next
                curNode.next = None
                preNode.next = curNode
                preNode = preNode.next
                l2 = nextNode
        return dummy.next
            