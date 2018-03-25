class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        for i in range(len(edges) - 1, -1, -1):
            if self.isGraph(edges[:i] + edges[i + 1:]):
                return edges[i]
    
    def isGraph(self, edges):
        father = [i for i in range(len(edges) + 1)]
        self.count = len(edges) + 1
        for edge in edges:
            self.merge(edge[0] - 1, edge[1] - 1, father)
        return self.count == 1
        
        
    def find(self, x, father):
        if father[x] == x:
            return father[x]
        father[x] = self.find(father[x], father)
        return father[x]
    
    def merge(self, a, b, father):
        root_a, root_b = self.find(a, father), self.find(b, father)
        if root_a != root_b:
            father[root_b] = root_a
            self.count -= 1
