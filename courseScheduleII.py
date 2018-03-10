class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        summary = {}
        degree = [0] * numCourses
        for pair in prerequisites:
            summary[pair[1]] = summary.get(pair[1], []) + [pair[0]]
            degree[pair[0]] += 1
        queue = []
        for num in range(numCourses):
            if degree[num] == 0:
                queue.append(num)
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node)
            if node in summary:
                for course in summary[node]:
                    degree[course] -= 1
                    if degree[course] == 0:
                        queue.append(course)
        if len(res) == numCourses:
            return res
        return []
