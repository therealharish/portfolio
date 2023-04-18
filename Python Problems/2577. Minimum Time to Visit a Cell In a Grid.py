class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        minHeap = []
        heappush(minHeap, (0, 0, 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
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
                if timeMat[newR][newC] > time+1:
                    if curr <= time+1:
                        timeMat[newR][newC] = time+1
                    else:
                        if grid[newR][newC] % 2 == time%2:
                            timeMat[newR][newC] = grid[newR][newC] + 1
                        else:
                            timeMat[newR][newC] = grid[newR][newC]
                    heappush(minHeap, (time+1, newR, newC))
        
        return -1
            
        
        