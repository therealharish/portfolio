class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            nums[i] = set(nums[i])
        
        for i in range(len(nums)):
            for k in nums[i]:
                flag = True
                for j in range(len(nums)):
                    if i != j:
                        if k not in nums[j]:
                            flag = False
                            break
                if flag:
                    ans.append(k)
        return ans
                    