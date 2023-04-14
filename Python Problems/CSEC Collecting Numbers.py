n = int(input())
arr = list(map(int, input().split()))

d = {}
for index, i in enumerate(arr):
    d[i] = index

count = 0
prev = d[1]
for i in range(2, n+1):
    if d[i] < prev:
        count += 1
    prev = d[i]
print(count+1)
    
    