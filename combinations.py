class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(n, 1, k, [], res)
        return res
    def helper(self, n, i, k, cur, res):
        if len(cur) == k:
            res.append(cur)
            return
        if i > n:
            return
        self.helper(n, i + 1, k, cur + [i], res)
        self.helper(n, i + 1, k, cur, res)
