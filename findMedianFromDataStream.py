import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap, self.minHeap = [], []
        self.count = 0
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.count % 2 == 0:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        self.count += 1
        if len(self.maxHeap) == 0 or len(self.minHeap) == 0:
            return
        if -self.maxHeap[0] > self.minHeap[0]:
            maxRoot, minRoot = -self.maxHeap[0], self.minHeap[0]
            heapq.heapreplace(self.maxHeap, -minRoot)
            heapq.heapreplace(self.minHeap, maxRoot)

    def findMedian(self):
        """
        :rtype: float
        """
        if self.count % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return -self.maxHeap[0]

