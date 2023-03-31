# old solution
class Solution1:

    def __init__(self):
        self.lcs = set([])

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if not s1 or len(s1) == 0:
            return sum([ord(char) for char in s2]) if s2 else 0

        if not s2 or len(s2) == 0:
            return sum([ord(char) for char in s1]) if s1 else 0

        total_s1, total_s2 = sum([ord(char) for char in s1]), sum([ord(char) for char in s2])
        l1, l2 = len(s1), len(s2)

        s1 = "#" + s1
        s2 = "#" + s2

        # dp initialziation
        # f[i][j] represents LCS with largest ascii from s1[:i] and s2[:j]
        f = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)] 

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if s1[i] == s2[j]:
                    f[i][j] = f[i - 1][j - 1] + ord(s1[i])
                else:
                    f[i][j] = max(
                        f[i - 1][j - 1],
                        f[i - 1][j],
                        f[i][j - 1]
                    )

        return total_s1 + total_s2 - 2 * f[l1][l2]


    def _get_all_lcs(self, f, s1, s2, l1, l2, curr):
        if l1 <= 0 or l2 <= 0:
            curr_lcs = curr[:][::-1]
            if curr_lcs not in self.lcs:
                self.lcs.add(curr_lcs)
            return

        if s1[l1] == s2[l2]:
            curr.append(s1[l1])
            self._get_lcs(f, s1, s2, l1 - 1, l2 - 1, curr)
            curr.pop()
        else:
            if f[l1 - 1][l2] > f[l1][l2 - 1]:
                self._get_lcs(f, s1, s2, l1 - 1, l2, curr)
            elif f[l1 - 1][l2] < f[l1][l2 - 1]:
                self._get_lcs(f, s1, s2, l1, l2 - 1, curr)
            else:
                self._get_lcs(f, s1, s2, l1 - 1, l2, curr)
                self._get_lcs(f, s1, s2, l1, l2 - 1, curr)


# new solution
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        temp = 0 
        for i in range(n1 - 1, -1, -1):
            temp += ord(s1[i])
            dp[i][n2] = temp 
        
        temp = 0
        for j in range(n2 - 1, -1, -1):
            temp += ord(s2[j]) 
            dp[n1][j] = temp 
            
        for i in range(n1 - 1, -1, -1):
            for j in range(n2-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))
        
        return dp[0][0]