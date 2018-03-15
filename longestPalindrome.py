class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        summary = {}
        for char in s:
            summary[char] = summary.get(char, 0) + 1
        flag = 1
        ans = 0
        for val in summary.values():
            if val % 2 == 0:
                ans += val
            else:
                if flag == 1:
                    ans += val
                    flag = 0
                else:
                    ans += val - 1
        return ans
