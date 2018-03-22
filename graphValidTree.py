class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        summary = {}
        for edge in edges:
            summary[edge[0]] = summary.get(edge[0], []) + [edge[1]]
            summary[edge[1]] = summary.get(edge[1], []) + [edge[0]]
        visited = {}
        visited[0] = True
        queue = [0]
        while queue:
            cur = queue.pop(0)
            if cur in summary:
                for node in summary[cur]:
                    if node not in visited:
                        visited[node] = True
                        queue.append(node)
        return len(visited) == n
