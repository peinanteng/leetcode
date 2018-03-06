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
        ans = 0
        # find the celebrity candidate
        for i in range(1, n):
            if Celebrity.knows(ans, i):
                ans = i
        
        flag = 1
        # identify whether somebody don't know the candidate
        for i in range(n):
            if i != ans and not Celebrity.knows(i, ans):
                flag = 0
                break
        # identify whether candidate knows any others
        for i in range(n):
            if i != ans and Celebrity.knows(ans, i):
                flag = 0
                break
        # return the celebrity if it exist, else -1
        if flag == 1:
            return ans
        else:
            return -1
                
        
