from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        q = PriorityQueue()
        
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            node = q.get()[1]
            cur.next = node
            cur = cur.next
            if cur.next:
                q.put((cur.next.val, cur.next))
        return dummy.next