class Solution1:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 1_000_000_007
        col = []
        for i in zip(*words):
            s = Counter()
            for j in i:
                s[j]+=1
            col.append(s)

        # Top-Down
        @cache
        def dfs(i,j):
            if j==len(target):
                return 1
            if i == len(words[0]):
                return 0

            t = dfs(i+1,j)
            if col[i][target[j]]>0:
                t += dfs(i+1,j+1)*col[i][target[j]]
            return t%mod
        return dfs(0,0)

        # Bottom-up
        dp = [[0]*(len(target)+1) for _ in range(len(words[0])+1)]
        for i in range(len(words[0]),-1,-1):
            for j in range(len(target),-1,-1):
                if j==len(target):
                    dp[i][j] = 1
                    continue
                if i == len(words[0]):
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i+1][j]
                if col[i][target[j]] > 0:
                    dp[i][j] += dp[i+1][j+1]*col[i][target[j]]
                dp[i][j] %= mod
        return dp[0][0]

        # Bottom-up(Space-optimized)
        dp = [0]*(len(target)+1)
        for i in range(len(words[0]),-1,-1):
            cur = [0]*(len(target)+1)
            for j in range(len(target),-1,-1):
                if j==len(target):
                    cur[j] = 1
                    continue
                if i == len(words[0]):
                    cur[j] = 0
                    continue
                cur[j] = dp[j]
                if col[i][target[j]] > 0:
                    cur[j] += dp[j+1]*col[i][target[j]]
                cur[j] %= mod
            dp = cur
        return dp[0]
    
# convert the above code to c++ 



class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 1_000_000_007
        col = []
        for i in zip(*words):
            s = Counter()
            for j in i:
                s[j]+=1
            col.append(s)

        dp = {}
        def dfs(i,j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j==len(target):
                return 1
            if i == len(words[0]):
                return 0

            t = dfs(i+1,j)
            if col[i][target[j]]>0:
                t += dfs(i+1,j+1)*col[i][target[j]]
            dp[(i, j)] = t%mod
            return dp[(i, j)]
        return dfs(0,0)
    