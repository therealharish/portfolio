class Solution1:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def helper(h, n, target):
            if target <= 0 or target > (n * k):
                return 0
            if n == 1:
                return 1
            if (n, target) in h:
                return h[(n, target)]
            res = 0
            for i in range(1, k + 1):
                res += helper(h, n - 1, target - i)
            h[(n, target)] = res
            return h[(n, target)]
        h = {}
        return helper(h, n, target) % (10 ** 9 + 7)

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @cache
        def solve(n, target):
            if target < 0:
                return 0
            if n == 0 and target == 0:
                return 1
            if n == 0 and target != 0:
                return 0
            
            res = 0
            for i in range(1, k+1):
                res += solve(n-1, target-i)
            return res 
        return solve(n, target) % (10**9 + 7)