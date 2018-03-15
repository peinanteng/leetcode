class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        edges = sorted(nums, reverse=True)
        ans = 0
        # assume i is the longest edge
        for i, length in enumerate(edges):
            # j, k is other two edges
            j, k = i + 1, i + 2
            # find the shortest length for k
            while k < len(edges) and length < edges[j] + edges[k]:
                k += 1
            k -= 1
            # for every j, when j += 1, find the shortest length for k
            while j < k:
                ans += k - j
                j += 1
                while j < k and edges[j] + edges[k] <= length:
                    k -= 1
        # return result
        return ans