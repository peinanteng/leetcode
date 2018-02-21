class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0

        minres = 2 ** 31
        cursum = 0
        for i in range(len(gas)):
            cursum += gas[i] - cost[i]
            if cursum < minres:
                minres = cursum
                start = i
        if start == len(gas) - 1:
            start = 0
        else:
            start += 1
        return start if cursum >= 0 else -1