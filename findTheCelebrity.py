# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0] * n
        # find the candidate who doesn't know anyone
        for i in range(n):
            j = 0
            while j < i:
                if nums[j] == 0 and knows(j, i):
                    nums[j] = 1
                j += 1
        index = 0
        while index < n - 1 and nums[n - 1] == 0:
            if knows(n - 1, index):
                nums[n - 1] = 1
            index += 1
        candidate = []
        for i in range(n):
            if nums[i] == 0:
                candidate.append(i)
        print(nums, candidate)
         # identify whether all other people knows the candidate
        celebrity = -1
        for i in candidate:
            j = 0
            while j >= 0 and j < n:
                if j == i:
                    j += 1
                elif knows(j, i):
                    j += 1
                else:
                    j = -1
            if j == n:
                celebrity = i
        return celebrity
        
