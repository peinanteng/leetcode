class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        #Initialise the flag value to any number
        queenFlag, kingFlag = 99, 88
        queenNum, kingNum = 0, 0
        for num in nums:
            if num == queenFlag:
                queenNum += 1
            elif num == kingFlag:
                kingNum += 1
            else:
                if queenNum == 0:
                    queenFlag = num
                    queenNum += 1
                elif kingNum == 0:
                    kingFlag = num
                    kingNum += 1
                else:
                    queenNum -= 1
                    kingNum -= 1
                    
        queenNum, kingNum = 0, 0
        for num in nums:
            if num == queenFlag:
                queenNum += 1
            elif num == kingFlag:
                kingNum += 1
        
        if queenNum > len(nums) // 3:
            res.append(queenFlag)
        if kingNum > len(nums) // 3:
            res.append(kingFlag)
        return res
