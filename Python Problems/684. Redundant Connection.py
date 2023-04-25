class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges)+1)]
        res = []
        def union(a, b):
            p1 = find(a)
            p2 = find(b)
            if p1!=p2:
                parent[p1] = p2
            else:
                res = [a, b]
        
        def find(a):
            if a == parent[a]:
                return a
            else:
                parent[a] = find(parent[a])
                return parent[a]
        
        for i, j in edges:
            union(i, j)    
        return res