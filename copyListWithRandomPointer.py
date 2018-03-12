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
            return None
        newHead = RandomListNode(head.label)
        summary = {}
        summary[head] = newHead
        p = head
        q = newHead
        while p:
            q.random = p.random
            if p.next:
                q.next = RandomListNode(p.next.label)
                summary[p.next] = q.next
            else:
                q.next = None
            p = p.next
            q = q.next
        q = newHead
        while q:
            if q.random:
                q.random = summary[q.random]
            q = q.next
        return newHead
                
          
