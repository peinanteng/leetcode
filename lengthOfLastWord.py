class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        index = len(s) - 1
        while index >= 0 and s[index] == ' ':
            index -= 1
        while index >= 0 and s[index] != ' ':
            result += 1
            index -= 1
        return result

