def transitionPoint(arr, n):
    
    i = arr[0]
    if i == 0:
        if 1 in arr:
            return arr.index(1)
        else:
            return -1
    else:
        if 0 in arr:
            return arr.index(0)
        else:
            return -1
    
arr = [0, 0, 0, 1, 1]
print(transitionPoint(arr, len(arr)))
      