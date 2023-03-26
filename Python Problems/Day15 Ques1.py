# longest zig zag subsequence
# given an array nums of n positive integers. The task is to find the longest zig zag subsequence present in the given array.
nums = [1, 5, 4]
nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
nums = [1, 9, 8, 10, 2, 4, 0, 5, 1]
nums = [2, 3, 4, 6, 10, 4, 5, 9, 6, 8, 3, 7, 4]
nums = [3, 8, 5, 9, 4,7,2,6]

def longestZigzag(nums):
    n = len(nums)
    dp = [[1,1] for _ in range(n)]
    print(dp)
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i][0] = max(dp[i][0], dp[j][1] + 1)
            elif nums[i] < nums[j]:
                dp[i][1] = max(dp[i][1], dp[j][0] + 1)
        print(dp)
    return max(max(dp))


def longestZigZagLinearTime(nums):
    n = len(nums)
    if n < 2:
        return n
    up = 1
    down = 1
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            up = down + 1
        elif nums[i] < nums[i-1]:
            down = up + 1
    return max(up, down)

# print(longestZigzag(nums))
print(longestZigZagLinearTime(nums))