<<<<<<< Updated upstream
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
=======
arr = [30, 11, 43, 32, 8, 15]
k = 3

def prefixSumOfLastKElement(arr):
    
    ans = [0] * len(arr)
    s = 0
    for i in range(k):
        s += arr[i]
    
    ans[k-1] = s
    minsofar = s/k
    index = 0
    leave = 0
    for i in range(k, len(arr)):
        print(minsofar)
        ans[i] = (ans[i-1] + arr[i] - arr[leave])
        if ans[i]/k < minsofar:
            minsofar = ans[i]/k
            index = i
        leave += 1
    print(ans)
    return (index-k+1, index)

print(prefixSumOfLastKElement(arr))
>>>>>>> Stashed changes


    
    