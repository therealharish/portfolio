n = int(input())
arr = list(map(int, input().split()))
r1 = int(input())
r2 = int(input())

def numbersInRange(arr, r1, r2):
    count = 0
    for i in arr:
        if i >= r1 and i <= r2:
            count+=1
    return count

print(numbersInRange(arr, r1, r2))
