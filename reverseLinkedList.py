# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        preNode, curNode = None, head
        while curNode:
            nextNode = curNode.next
            curNode.next = preNode
            preNode, curNode= curNode, nextNode
        return preNode
