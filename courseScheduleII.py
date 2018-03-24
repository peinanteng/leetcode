from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        summary = {}
        degree = [0] * numCourses
        for x, y in prerequisites:
            summary[y] = summary.get(y, []) + [x]
            degree[x] += 1
        queue = deque([])
        for num in range(numCourses):
            if degree[num] == 0:
                queue.append(num)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            if node in summary:
                for course in summary[node]:
                    degree[course] -= 1
                    if degree[course] == 0:
                        queue.append(course)
        if len(res) == numCourses:
            return res
        return []
