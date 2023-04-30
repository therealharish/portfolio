class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        originalEdges = edges[:]
        edges = sorted(edges, key = lambda x: x[2])
        def kruskalUsingDSU(edges):
            
            parent = [i for i in range(n)]
            
            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            
            def union(x, y):
                p1 = find(x)
                p2 = find(y)
                if p1!=p2:
                    parent[p2] = p1
                    return True
                else:
                    False
            
            mst = []
            cost = 0
            for u, v, w in edges:
                if union(u, v):
                    cost += w
            return cost
        
        originalCost = kruskalUsingDSU(edges)
        critical = []
        pseudoCritical = []
        for i in range(len(originalEdges)):
            
            exclude = kruskalUsingDSU(originalEdges[:i] + originalEdges[i+1:])
            include = kruskalUsingDSU([originalEdges[i]] + originalEdges[0:i] + originalEdges[i+1:])
            
            if exclude > originalCost or exclude < originalCost:
                critical.append(i)
            elif include == originalCost:
                pseudoCritical.append(i)
                
        return [critical, pseudoCritical]
            
                
        
        
        
        