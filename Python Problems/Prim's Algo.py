from heapq import heappush, heappop

edge = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]
n = 9

def prims(edge, n):
    adj = {i:[] for i in range(n)}
    for src, dst, dist in edge:
        adj[src].append((dst, dist))
        adj[dst].append((src, dist))
    
    minHeap = []

    distance = [float('inf')]*n
    parent = [-1]*n
    mstSet = [False]*n

    distance[0] = 0

    heappush(minHeap, (0, 0))

    while(minHeap):
        currDist, currNode = heappop(minHeap)
        if mstSet[currNode]:
            continue
        mstSet[currNode] = True
        for nbr, dist in adj[currNode]:
            if mstSet[nbr]:
                continue
            if distance[nbr] > dist:
                distance[nbr] = dist
                parent[nbr] = currNode
                heappush(minHeap, (dist, nbr))
                
    return (parent, distance)

parent, distance = prims(edge, n)
print(parent, distance)
            
        