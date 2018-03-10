class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        result = self.nums[:]
        return result

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        result = self.reset()
        length = len(result)
        import random
        for i in range(length - 1, - 1, -1):
            j = random.randint(0, i)
            result[i], result[j] = result[j], result[i]
        return result
    
        

