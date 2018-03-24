# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        node = head
        while node:
            nextNode = node.next
            node.next = RandomListNode(node.label)
            node.next.next = nextNode
            node = nextNode
        node = head
        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next
        newHead = head.next
        node1, node2 = head, newHead
        cur = node1.next.next
        while cur:
            node1.next = cur
            node2.next = cur.next
            node1 = node1.next
            node2 = node2.next
            cur = cur.next.next
        node1.next = None
        return newHead
                
          
