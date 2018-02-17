class MinHeap():
    def __init__(self, nums):
        self.nums = nums
        self.MAX = max(nums) + 1
        self.heapify()

    def heapify(self):
        nums = self.nums
        startIndex = len(nums) // 2
        for i in range(startIndex, -1, -1):
            self.bubbledown(i)

    def bubbledown(self, index):
        nums = self.nums
        while True:
            curVal = nums[index]
            left = index * 2 + 1
            right = index * 2 + 2
            leftVal = nums[left] if left < len(nums) else self.MAX
            rightVal = nums[right] if right < len(nums) else self.MAX

            if leftVal > curVal and rightVal > curVal:
                break
            if leftVal > rightVal:
                nums[right], nums[index] = nums[index], nums[right]
                index = right
            else:
                nums[left], nums[index] = nums[index], nums[left]
                index = left

heap = MinHeap([9,8,7,6,5,4,3,2,1])
print(heap.nums)
pass