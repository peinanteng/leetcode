class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                pre = stack.pop()
                if char == ')' and pre != '(':
                    return False
                elif char == ']' and pre != '[':
                    return False
                elif char == '}' and pre != '{':
                    return False
        if stack:
            return False
        return True