class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = pre = ListNode(0)
        cur = head
        while cur:
            if cur.next == None:
                pre.next = cur
                cur = None
            else:
                nextnextnode = cur.next.next
                nextnode = cur.next
                cur.next.next = None
                cur.next = None
                pre.next = nextnode
                pre.next.next = cur
                pre = pre.next.next
                cur = nextnextnode
            
        return dummy.next