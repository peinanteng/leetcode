class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        summary = {}
        queue = []
        degree = [0] * numCourses
        for x, y in prerequisites:
            summary[y] = summary.get(y, []) + [x]
            degree[x] += 1
        for course in range(numCourses):
            if degree[course] == 0:
                queue.append(course)
        count = 0
        while queue:
            course = queue.pop(0)
            count += 1
            if course in summary:
                for c in summary[course]:
                    degree[c] -= 1
                    if degree[c] == 0:
                        queue.append(c)
        return count == numCourses
