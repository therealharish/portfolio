def find(arr):
    
    m = min(arr)
    ans = arr.index(m)
    
    return (m, ans)

m, ans = find([1,2,3,4,5])
print(m)
print(ans)

