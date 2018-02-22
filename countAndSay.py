class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 1:
            return '1'
        prestr = self.countAndSay(n - 1)
        
        cur_char = prestr[0]
        count = 1
        ans = ''
        for char in prestr[1:]:
            if char == cur_char:
                count += 1
            else:
                ans += str(count) + cur_char
                cur_char = char
                count = 1
        ans += str(count) + cur_char
        return ans
                
