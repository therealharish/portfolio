class Solution1:
    def minInsertions(self, s: str) -> int:

        @cache
        def solve(i, j):
            if i>j:
                return 0
            if i == j:
                return 1
            if s[i]==s[j]:
                return 2 + solve(i+1, j-1)
            
            return max(solve(i+1, j-1), solve(i+1, j), solve(i, j-1))

        count = solve(0, len(s)-1)
        return len(s)-count
    
    # tabulate this code
    

        
# tabulation
# class Solution:
#     def minInsertions(self, s: str) -> int:

#         dp = [[0 for i in range(len(s))] for j in range(len(s))]

#         for i in range(len(s)-1, -1, -1):
#             for j in range(len(s)):
                
#                 if i>j:
#                     dp[i][j] = 0
#                 elif i == j:
#                     dp[i][j] = 1
#                 elif s[i] == s[j]:
#                     dp[i][j] = 2 + dp[i+1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i+1][j-1], dp[i+1][j], dp[i][j-1])

#         return len(s) - dp[0][0]


        
