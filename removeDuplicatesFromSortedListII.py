# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        preVal = head.val - 1
        dummy = preNode = ListNode(preVal)
    
        curNode = head
        while curNode:
            curVal = curNode.val
            if curVal == preVal:
                curNode = curNode.next
            else:
                preVal = curVal
                if curNode.next == None or curNode.next.val != curVal:
                    preNode.next = curNode
                    preNode = curNode
                curNode = curNode.next
        preNode.next = None
        return dummy.next
