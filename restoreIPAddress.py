class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.helper(s, 4, "", res)
        return res

    def helper(self, s, n, cur, res):
        if n == 0 and len(s) == 0:
            res.append(cur[1:])
            return
        if len(s) < n or len(s) > 3 * n:
            return
        self.helper(s[1:], n - 1, cur[:] + '.' + s[0], res)
        if len(s) > 1 and s[0] != '0':
            self.helper(s[2:], n - 1, cur[:] + '.' + s[:2], res)
        if len(s) > 2 and s[0] != '0':
            if int(s[:3]) <= 255:
                self.helper(s[3:], n - 1, cur[:] + '.' + s[:3], res)
