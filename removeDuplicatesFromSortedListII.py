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
        dummy = ListNode(2 ** 31 + 1)
        preNode = dummy
        
        preVal = 2 ** 31 + 1
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
        
