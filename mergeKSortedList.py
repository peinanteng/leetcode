# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        dummy = preNode = ListNode(0)
        preNode.next = None
        self.heap = []
        self.MAX = 2 ** 31
        for node in lists:
            if node:
                self.heap.append(node)
        if self.heap:
            self.heapify()
        while self.heap:
            node = self.heapPop()
            nextNode = node.next
            if nextNode:
                self.heapAdd(nextNode)
            node.next = None
            preNode.next = node
            preNode = preNode.next
        return dummy.next
    
    def heapify(self):
        startIndex = len(self.heap) // 2
        for index in range(startIndex, -1, -1):
            self.bubbleDown(index)
    def heapPop(self):
        heap = self.heap
        heap[0], heap[-1] = heap[-1], heap[0]
        node = heap.pop()
        self.bubbleDown(0)
        return node
    def heapAdd(self, node):
        heap = self.heap
        heap.append(node)
        self.bubbleUp(len(heap) - 1)
    def bubbleDown(self, index):
        heap = self.heap
        while index < len(heap):
            curVal = heap[index].val
            left, right = index * 2 + 1, index * 2 + 2
            leftVal = heap[left].val if left < len(heap) else self.MAX + 1
            rightVal = heap[right].val if right < len(heap) else self.MAX + 1
            if curVal < leftVal and curVal < rightVal:
                break
            if leftVal >= rightVal:
                heap[index], heap[right] = heap[right], heap[index]
                index = right
            else:
                heap[index], heap[left] = heap[left], heap[index]
                index = left
    
    def bubbleUp(self, index):
        heap = self.heap 
        while index > 0:
            curVal = heap[index].val
            paren = (index - 1) // 2
            parenVal = heap[paren].val
            if parenVal > curVal:
                heap[index], heap[paren] = heap[paren], heap[index]
                index = paren
            else:
                break
            
            
        