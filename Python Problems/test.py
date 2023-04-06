class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        bfsVisit = set()
        q = deque()
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0 or i == row-1 or j == col-1:
                    if grid[i][j] == 0:
                        q.append((i, j))
                        bfsVisit.add((i, j))
                        
                        
        print(q) 
        while q:
            r, c = q.popleft()
            print(r, c)
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 1 or (r, c) in bfsVisit:
                continue
            grid[r][c] = 1
            bfsVisit.add((r, c))
            for dr, dc in directions:
                newR, newC = r+dr, c+dc
                q.append((newR, newC))

        for i in range(row):
            print(grid[i])
        
        

        def dfs(i, j):
            if i < 0 or j< 0 or i>=row-1 or j>=col-1 or grid[i][j] == 1:
                return
            if (i, j) not in visited:
                visited.add((i, j))
                for dr, dc in directions:
                    r = i+dr
                    c = j+dc
                    dfs(r, c)
        
        visited = set()
        count = 0
        for i in range(row-1):
            for j in range(col-1):
                if i == 0 or j == 0:
                    continue
                if grid[i][j] == 0 and (i, j) not in visited:
                    # print(i, j)
                    dfs(i, j)
                    count+=1
        return count
        