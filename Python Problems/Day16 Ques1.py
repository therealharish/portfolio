# first element to occur k times
k = 2
d = {}
arr = [1, 7, 4, 3, 4, 8, 7]
best = -1

def firstElement(k, d, arr):
    for i in range(len(arr)-1, -1, -1):
        curr = arr[i]
        d[curr] = d.get(curr, 0) + 1
        if d[curr]>=k:
            best = curr
    return best

best = firstElement(k, d, arr)
print(best)
    