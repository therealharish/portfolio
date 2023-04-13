class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        next = [0 for _ in range(len(arr))]
        d = {}
        d[0] = 0
        for i in range(1, len(arr)):
            if arr[i] + difference in d:
                next[i] = d[i]
                d[arr[i]] = i
        print(next)
        
            