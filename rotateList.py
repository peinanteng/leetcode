class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        count = 0
        curNode = head
        while curNode:
            count += 1
            curNode = curNode.next
        
        target = count - k % count
        count = 1
        preNode, curNode = None, head
        while curNode and count <= target:
            count += 1
            preNode, curNode = curNode, curNode.next
        preNode.next = None
        
        dummy = ListNode(0)
        dummy.next = curNode
        
        preNode, curNode = dummy, dummy.next
        while curNode:
            preNode, curNode = curNode, curNode.next
        
        preNode.next = head
        return dummy.next
        
        
        
