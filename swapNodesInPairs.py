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
        if head is None or head.next == None:
            return head
        dummy = ListNode(0)
        curNode1, curNode2 = head, head.next
        pre = dummy
        while curNode2:
            pre.next = curNode2
            nextNode = curNode2.next
            curNode2.next = curNode1
            curNode1.next = nextNode
            if nextNode:
                pre = curNode1
                curNode1 = nextNode
                curNode2 = nextNode.next    
            else:
                break
        return dummy.next