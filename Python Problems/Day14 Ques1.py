n = 32
n = 45

# using and 
def findIFNumberIsPowerOfTwo1(n):
    if n & (n-1):
        print("No")
    else:
        print("Yes")

#by counting number of set bits
def findIFNumberIsPowerOfTwo2(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    if count == 1:
        print("Yes")
    else:
        print("No")
        
findIFNumberIsPowerOfTwo2(n)