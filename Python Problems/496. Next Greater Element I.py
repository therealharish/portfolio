class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def nextGreatestElement(arr):
            stack = []
            ans = [-1] * len(arr)
            
            for i in range(len(arr)):
                curr = arr[i]
                while stack and curr > arr[stack[-1]]:
                    ans[stack.pop()] = curr
                stack.append(i)
            
            return ans
        
        arr = nextGreatestElement(nums2)
        ans = []
        for i in nums1:
            if i in nums2:
                ans.append(arr[nums2.index(i)])
        return ans