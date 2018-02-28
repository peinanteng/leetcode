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
                nextnode1 = node1.next
                nextnode2 = node2.next
                node1.next = node2
                node2.next = nextnode1
                node1 = nextnode1
                node2 = nextnode2
