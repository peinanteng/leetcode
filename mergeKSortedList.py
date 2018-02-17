# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        self.heap = []
        self.MAX = 2 ** 31
        self.MIN = -2 ** 31 - 1
        if not lists:
            return
        for list in lists:
            if list:
                self.heap.append(list)

        if self.heap:
            self.heapify()
        dummy = pre = ListNode(0)
        dummy.next = None
        while self.heap:
            curNode = self.heapPop()
            pre.next = ListNode(curNode.val)
            if curNode.next:
                self.heapAdd(curNode.next)
            pre = pre.next
        return dummy.next

    def heapify(self):
        startIndex = len(self.heap) // 2
        for i in range(startIndex, -1, -1):
            self.bubbleDown(i)

    def heapPop(self):
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            node = self.heap.pop()
            self.bubbleDown(0)
            return node
    def heapAdd(self, node):
            self.heap.append(node)
            self.bubbleUP(len(self.heap) - 1)
    def bubbleDown(self, index):
        while index < len(self.heap):
            curVal = self.heap[index].val
            left, right = index * 2 + 1, index * 2 + 2
            leftVal = self.heap[left].val if left < len(self.heap) else self.MAX + 1
            rightVal = self.heap[right].val if right < len(self.heap) else self.MAX + 1

            if leftVal >= curVal and rightVal >= curVal:
                break
            if leftVal >= rightVal:
                self.heap[right], self.heap[index] = self.heap[index], self.heap[right]
                index = right
            else:
                self.heap[left], self.heap[index] = self.heap[index], self.heap[left]
                index = left
    def bubbleUP(self, index):
        while index > 0:
            paren = (index - 1) // 2
            curVal = self.heap[index].val
            parenVal = self.heap[paren].val
            if curVal >= parenVal:
                break
            else:
                self.heap[index], self.heap[paren] = self.heap[paren], self.heap[index]
                index = paren