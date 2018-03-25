class Solution(object):
    def __init__(self):
        self.father = []
        self.count = 0
    
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def merge(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_b] = root_a
            self.count -= 1
        
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        for i in range(n):
            self.father.append(i)
            self.count += 1
        for node1, node2 in edges:
            self.merge(node1, node2)
        return self.count
