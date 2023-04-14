class Solution1:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for i in range(len(nums)):
            if(nums[i]<=first):
                first = nums[i]
            elif(nums[i]<=second):
                second = nums[i]
            else:
                return True
        return False
            
            
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        st = []
        st.append(nums[0])
        for i in range(1, len(nums)):
            print(st)
            if nums[i] > st[-1]:
                st.append(nums[i])
                if len(st) == 3:
                    return True
            else:
                while (st and st[-1] > nums[i]):
                    st.pop()
                st.append(nums[i])
        return False
                
    