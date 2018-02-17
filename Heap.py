class MaxHeap():
    def __init__(self):
        self.nums = []

    def push(self, num):
        self.nums.append(num)
        if len(self.nums) <= 1:
            return
        self.bubbleUp()

    def bubbleUp(self):
        nums = self.nums
        curIndex = len(nums) - 1
        while curIndex > 0:
            curVal = nums[curIndex]
            parentIndex = (curIndex - 1) // 2
            parentVal = nums[parentIndex]
            if curVal <= parentVal:
                break
            nums[parentIndex], nums[curIndex] = nums[curIndex], nums[parentIndex]
            curIndex = parentIndex

heap = MaxHeap()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    heap.push(num)
    print(heap.nums)
