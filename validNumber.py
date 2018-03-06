class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        flag = 0
        #remove the spaces
        s = s.strip()
        # if there is a '+' or '-'
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            i += 1
        # find all the number before '.' or 'e'
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
            flag = 1
            i += 1
        # if there is a '.'
        if i < len(s) and s[i] == '.':
            i += 1
            # find all the digit after '.'
            while i < len(s) and s[i] >= '0' and s[i] <= '9':
                flag = 1
                i += 1
        # if find no number before e, return False
        if not flag:
            return False
        # if there is a 'e'
        if i < len(s) and s[i] == 'e':
            # indicate whether there is number after e
            flag = 0
            i += 1
            if i < len(s) and (s[i] == '-' or s[i] == '+'):
                i += 1
            while i < len(s) and s[i] >= '0' and s[i] <= '9':
                i += 1
                flag = 1
        # if there is number, and comes to the end
        if i > 0 and i == len(s) and flag:
            return True
        return False
