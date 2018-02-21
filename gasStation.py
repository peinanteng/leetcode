class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        nums = []
        for i in range(len(gas)):
            nums.append(gas[i] - cost[i])
        start = 0
        # while start < len(nums) and nums[start] < 0:
        #     start += 1
        # minres = sum(nums[:start])
        minres = 2 ** 31
        cursum = 0
        summary = {}
        for i in range(len(nums)):
            cursum += nums[i]
            if cursum not in summary:
                summary[cursum] = i
            if cursum < minres:
                minres = cursum
                start = i
        if start == len(nums) - 1:
            start = 0
        else:
            start += 1
        return start if cursum >= 0 else -1
