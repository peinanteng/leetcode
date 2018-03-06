# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i, i4, n4 = 0, 0, 0
        buf4 = [0] * 4
        while i < n:
            if i4 == n4:
                n4 = read4(buf4)
                i4 = 0
                if n4 == 0:
                    break
            buf[i] = buf4[i4]
            i += 1
            i4 += 1
        return i
