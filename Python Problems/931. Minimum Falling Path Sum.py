class Solution1:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                elif j == 0 and j+1<n:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
                elif j == n-1 and j-1>=0:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + matrix[i][j]
                elif j>0 and j<n-1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
                else:
                    dp[i][j] = dp[i-1][j]+matrix[i][j]
        #         print(dp)
        # print(dp)
        return min(dp[-1])


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        
        def solve(i, j):
            
            if i < 0 or i>=m or j<0 or j>=n:
                return float('inf')
            
            if i == m-1:
                return matrix[i][j]
            
            return matrix[i+1][j] + min(solve(i+1, j-1), solve(i+1, j), solve(i+1, j+1))


        ans = float('inf')
        for j in range(n):
            ans = min(ans, solve(0, j))
        
        return ans
