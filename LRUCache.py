class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.heap = []
        self.size = capacity
        self.summary = {}
        self.operation = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.summary:
            return -1
        self.operation += 1
        i = self.summary[key][0]
        self.heap[i][0] = self.operation
        self.bubbleDown(self.heap, i)
        return self.summary[key][1]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.operation += 1
        if key in self.summary:
            self.summary[key][1] = value
            self.heap[self.summary[key][0]][0] = self.operation
            self.bubbleDown(self.heap, self.summary[key][0])
        else:
            if len(self.heap) < self.size:
                self.heap.append([self.operation, key])
                self.summary[key] = [len(self.heap) - 1, value]
            else:
                del self.summary[self.heap[0][1]]
                self.heap[0] = [self.operation, key]
                self.summary[key] = [0, value]
                self.bubbleDown(self.heap, 0)
    
    def bubbleDown(self, heap, i):
        while True:
            leftChild = i * 2 + 1
            rightChild = i * 2 + 2
            leftVal = heap[leftChild][0] if leftChild < len(heap) else 2 ** 31 + 1
            rightVal = heap[rightChild][0] if rightChild < len(heap) else 2 ** 31 + 1
            curVal = heap[i][0]
            if curVal < leftVal and curVal < rightVal:
                break
            if leftVal < rightVal:
                self.summary[heap[leftChild][1]][0] = i
                self.summary[heap[i][1]][0] = leftChild
                heap[leftChild], heap[i] = heap[i], heap[leftChild]
                i = leftChild
            else:
                self.summary[heap[rightChild][1]][0] = i
                self.summary[heap[i][1]][0] = rightChild
                heap[rightChild], heap[i] = heap[i], heap[rightChild]
                i = rightChild
        
