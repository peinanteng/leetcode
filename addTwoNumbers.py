class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            cursum = 0
            if l1:
                cursum += l1.val
                l1 = l1.next
            if l2:
                cursum += l2.val
                l2 = l2.next
            if carry:
                cursum += carry
                carry 0
            if cursum >= 10:
                cursum -= 10
                carry = 1
            cur.next = ListNode(cursum)
            cur = cur.next
        cur.next = None
        return dummy.next
