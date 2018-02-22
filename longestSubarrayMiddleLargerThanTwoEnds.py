class Solution():
    def longestSubarrayMiddleLargerThanLeftAndRightEnd(self, nums):
        res = 0
        start = 0
        index = 0
        while start < len(nums):
            index = start + 1
            while index < len(nums) and nums[index] > nums[start]:
                index += 1
            if index < len(nums):
                if index - start + 1 > res:
                    res = index - start + 1
                start = index
            else:
                break
        if start < len(nums):
            end = len(nums) - 1
            while end > start:
                index = end - 1
                while nums[index] >= nums[end]:
                    index -= 1
                if index >= start:
                    if end - index + 1 >= res:
                        res = end - index + 1
                    end = index
                else:
                    break
        return res
