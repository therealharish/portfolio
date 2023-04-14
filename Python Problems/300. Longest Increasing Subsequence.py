# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#       dp = [1]*len(nums)
#       for i in range(len(nums)-1, -1, -1):
#         for j in range(i+1, len(nums)):
#           if(nums[j]>nums[i]):
#             dp[i] = max(1+dp[j], dp[i])
#       return max(dp)

# in notes 1 page 3
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#       ans = 0
#       m = 0
#       memo = [0]*len(nums)
#       for i in range(len(nums)):
#         for j in range(i):
#           if(nums[i]>nums[j] and m<memo[j]):
#             m = memo[j]
#         memo[i] = m+1
#         ans = max(ans, memo[i])
#       return ans


# in notes 1  pg 5 method 2
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def f1(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            return max(f1(n-1), 1+f2(n-1, nums[n-1]))
        
        @cache
        def f2(n, prev):
            if n == 0:
                return 0
            if nums[n-1] < prev:
                return max(f2(n-1, prev), 1+f2(n-1, nums[n-1]))
            else:
                return f2(n-1, prev)
            
        return f1(len(nums))
            
        