class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        adj = defaultdict(list)
        
        for i, num in enumerate(nums):
            adj[num].append(i)
        
        arr = []
        for index, i in enumerate(nums):
            if len(adj[i]) == 1:
                arr.append(0)
                
            else:
                a = 0
                for j in adj[i]:
                    a += abs(index - j)
                arr.append(a)
        
        return arr
        
            
# optimized solution

