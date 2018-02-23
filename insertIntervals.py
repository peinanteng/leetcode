
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        index = 0
        while index < len(intervals) and intervals[index].start <= newInterval.start:
            result.append(intervals[index])
            index += 1
        if not result:
            result.append(newInterval)
        else:
            if newInterval.start <= result[-1].end:
                result[-1].end = max(newInterval.end, result[-1].end)
            else:
                result.append(newInterval)
        
        while index < len(intervals):
            if intervals[index].start <= result[-1].end:
                result[-1].end = max(intervals[index].end, result[-1].end)
                index += 1
            else:
                result.append(intervals[index])
                index += 1
        return result
                
