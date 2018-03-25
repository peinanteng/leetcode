# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        root = UndirectedGraphNode(node.label)
        stack = [node]
        summary = {}
        summary[node.label] = root
        while stack:
            cur = stack.pop()
            for nei in cur.neighbors:
                if nei.label not in summary:
                    stack.append(nei)
                    summary[nei.label] = UndirectedGraphNode(nei.label)
                summary[cur.label].neighbors.append(summary[nei.label])
        return root
                
