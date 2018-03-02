class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curNum = nums[0]
        count = 0
        for num in nums[1:]:
            if num == curNum:
                count += 1
            else:
                if count == 0:
                    curNum = num
                    count += 1
                else:
                    count -= 1
        return curNum
