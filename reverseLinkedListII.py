# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        preNode, curNode = dummy, head
        count = 1
        while curNode and count < m:
            count += 1
            preNode, curNode = curNode, curNode.next
        startPre, start = preNode, curNode
        while curNode and count < n:
            count += 1
            curNode = curNode.next
        end, endNext = curNode, curNode.next
        
        startPre.next = end
        end.next = None
        
        preNode, curNode = endNext, start
        while curNode:
            nextNode = curNode.next
            curNode.next = preNode
            preNode, curNode = curNode, nextNode
        
        start.next = endNext
        return dummy.next
