class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        edges = sorted(nums, reverse=True)
        ans = 0
        for index, longest in enumerate(edges):
            i, j = index + 1, index + 2
            while j < len(edges) and longest < edges[i] + edges[j]:
                j += 1
            j -= 1
            while i < j:
                ans += j - i
                i += 1
                while i < j and edges[i] + edges[j] <= longest:
                    j -= 1
        return ans
