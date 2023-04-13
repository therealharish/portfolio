class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        minHeap = []
        heappush(minHeap, (0, 0, 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        timeMat = [[float('inf') for _ in range(col)] for _ in range(row)]
        timeMat[0][0] = 0
        while(minHeap):
            time, x, y = heappop(minHeap)
            
            if time > timeMat[x][y]:
                continue
            
            if x == row - 1 and y == col - 1:
                return time
            for i, j in directions:
                newR, newC = x + i, y + j
                if newR < 0 or newC < 0 or newR >= row or newC >= col:
                    continue
                curr = grid[newR][newC]
                if curr <= time+1:
                    time[newR][newC] = time+1
                    heappush(minHeap, (time+1, newR, newC))
                    
        return -1
            
        
        