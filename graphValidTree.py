class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        root = [i for i in range(n)]
        for edge in edges:
            root1 = self.find(root, edge[0])
            root2 = self.find(root, edge[1])
            if root1 == root2:
                return False
            root[root2] = root1
        return len(edges) == n - 1
    
    def find(self, root, e):
        if root[e] == e:
            return e
        root[e] = self.find(root, root[e])
        return root[e]
