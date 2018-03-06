class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # write a recursion function
        # recursion end condition
        if n <= 1:
            return '1'
        # find the previous result
        prestr = self.countAndSay(n - 1)
        # initialise current char and count
        cur_char = prestr[0]
        count = 1
        ans = ''
        for char in prestr[1:]:
            # if char equals current char, update count
            if char == cur_char:
                count += 1
            # if there is a new char, update the answer
            else:
                ans += str(count) + cur_char
                cur_char = char
                count = 1
        # update the answer
        ans += str(count) + cur_char
        return ans
                
