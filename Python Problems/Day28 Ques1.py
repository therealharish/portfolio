arr = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]

def secondMostRepeated(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    d = sorted(d.items(), key = lambda x: x[1], reverse = True)
    print(d)
    return d[1][0]

print(secondMostRepeated(arr))