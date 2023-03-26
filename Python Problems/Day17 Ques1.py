from heapq import heappush, heappop, heapify
arr = [7, 10, 4, 3, 20, 15]
k = 3

maxHeap = []

for i in arr:
    heappush(maxHeap, -i)

def findkthSmallest(k, maxHeap):
    for i in range(k):
        heappop(maxHeap)    
    return -maxHeap[0]

print(findkthSmallest(k, maxHeap))

