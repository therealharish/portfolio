arr = [1, 5, 7, 1]
k = 6

d = {}
for i in arr:
    d[i] = k-i
    
s = set(d.values())
count = 0
for i in arr:
    if i in s:
        count+=1
        s.remove(i)

print(count)