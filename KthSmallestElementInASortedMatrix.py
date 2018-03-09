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
        heap = []
        for i in range(m):
            self.heapAdd(heap, (matrix[i][0], i, 0))
        while k > 1:
            minItem = self.heapPop(heap)
            x, y = minItem[1], minItem[2]
            if y + 1 < n:
                self.heapAdd(heap, (matrix[x][y + 1], x, y + 1))
            k -= 1
        return self.heapPop(heap)[0]
    
    def heapAdd(self, heap, item):
        heap.append(item)
        self.bubbleUp(heap, len(heap) - 1)
    
    def heapPop(self, heap):
        length = len(heap) - 1
        heap[0], heap[length] = heap[length], heap[0]
        item = heap.pop()
        self.bubbleDown(heap, 0)
        return item
    
    def bubbleUp(self, heap, index):
        while index > 0:
            paren = (index - 1) // 2
            if heap[index][0] < heap[paren][0]:
                heap[index], heap[paren] = heap[paren], heap[index]
                index = paren
            else:
                break
    
    def bubbleDown(self, heap, index):
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
            
