class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        grid = dungeon
        row = len(dungeon)
        col = len(dungeon[0])
        
        def solve(i, j):
            
            if i < 0 or j < 0 or i >= row or j >= col:
                return float('inf')
            if i == row -1 and j == col - 1:
                return max(1, 1-grid[i][j])
            
            return max(1, min(solve(i+1, j) - grid[i][j], solve(i, j+1)-grid[i][j]))
            
        return solve(0, 0)