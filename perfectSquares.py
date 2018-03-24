from collections import deque
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.isPerfectSquare(n):
            return 1
        dq = deque([[n]])
        while dq:
            nums = dq.popleft()
            num = nums.pop()
            i = int(nums[-1] ** 0.5) if nums else 1
            while i * i <= num // 2:
                num1, num2 = i * i, num - i * i
                if self.isPerfectSquare(num2):
                    return len(nums) + 2
                else:
                    tempNums = nums[:]
                    tempNums.append(num1)
                    tempNums.append(num2)
                    dq.append(tempNums)
                i += 1
    def isPerfectSquare(self, num):
        if num < 1:
            return False
        left, right = 1, num
        while left + 1 < right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        if left * left == num or right * right == num:
            return True
        return False
            
