class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastStart = -1
        res = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                if lastStart == -1:
                    stack.append(i)
                else:
                    stack.append(lastStart)
                    lastStart = -1
            else:
                if stack:
                    tempstart = stack.pop()
                    res = max(res, i - tempstart + 1)
                    lastStart = tempstart
                else:
                    lastStart = -1
        return res
                
