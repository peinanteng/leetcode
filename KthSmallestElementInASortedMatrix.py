class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        heap = Heap()
        for i in range(m):
            heap.add((matrix[i][0], i, 0))
        while k > 1:
            _, x, y = heap.pop()
            if y + 1 < n:
                heap.add((matrix[x][y + 1], x, y + 1))
            k -= 1
        return heap.pop()[0]
    
class Heap(object):
    def __init__(self):
        self.heap = []

    def add(self, item):
        self.heap.append(item)
        self.bubbleUp(len(self.heap) - 1)

    def pop(self):
        heap = self.heap
        heap[0], heap[-1] = heap[-1], heap[0]
        item = self.heap.pop()
        self.bubbleDown(0)
        return item

    def bubbleUp(self, index):
        heap = self.heap
        while index > 0:
            paren = (index - 1) // 2
            if heap[index][0] < heap[paren][0]:
                heap[index], heap[paren] = heap[paren], heap[index]
                index = paren
            else:
                break

    def bubbleDown(self, index):
        heap = self.heap
        while index < len(heap):
            leftChild = index * 2 + 1
            rightChild = index * 2 + 2
            curVal = heap[index][0]
            leftVal = heap[leftChild][0] if leftChild < len(heap) else 2 ** 31 + 1
            rightVal = heap[rightChild][0] if rightChild < len(heap) else 2 ** 31 + 1
            if curVal < leftVal and curVal < rightVal:
                break
            elif leftVal >= rightVal:
                heap[rightChild], heap[index] = heap[index], heap[rightChild]
                index = rightChild
            else:
                heap[leftChild], heap[index] = heap[index], heap[leftChild]
                index = leftChild
