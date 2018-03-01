class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        soldierFlag = 0
        soldierNum = 0
        for num in nums:
            if num == soldierFlag:
                soldierNum += 1
            else:
                if soldierNum == 0:
                    soldierFlag = num
                    soldierNum += 1
                else:
                    soldierNum -= 1
        return soldierFlag
