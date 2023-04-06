
n = int(input())
arr = list(map(int,input().split()))

adj = {}
for i in range(n-1):
    fromm = arr[i]
    to = arr[i+1]
    if not i & 1:
        adj[fromm] = to
print(adj)

dp = {}
def minSnakeAndLadder(i):
    if i >= 30:
        return 0
    if i in dp:
        return dp[i]
    if i in adj:
        if i < adj[i]:
            dp[i] = minSnakeAndLadder(adj[i])
            return dp[i]
    
    dp[i]=  1 + min(minSnakeAndLadder(i+1), minSnakeAndLadder(i+2), minSnakeAndLadder(i+3), minSnakeAndLadder(i+4), minSnakeAndLadder(i+5), minSnakeAndLadder(i+6))
    return dp[i]

print(minSnakeAndLadder(1))           
