# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head:
            slow, fast = head, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            preNode, curNode = None, slow.next
            slow.next = None
            while curNode:
                nextNode = curNode.next
                curNode.next = preNode
                preNode, curNode = curNode, nextNode
            node1, node2 = head, preNode
            while node2:
                nextNode1 = node1.next
                nextNode2 = node2.next
                node1.next = node2
                node2.next = nextNode1
                node1 = nextNode1
                node2 = nextNode2
