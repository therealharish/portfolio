s1 = "geeksforgeeks"
s2 = "set"

# s1 = "adcffaet"
# s2 = "onkl"

def minimumIndexedCharacter(s1, s2):
    index = float('inf')
    stringSet = set(s1)
    for i in s2:
        if i in stringSet:
            index = min(index, s1.index(i))
    return -1 if index == float('inf') else index

def minimumIndexedCharacterWithDict(s1, s2):
    d = {}
    minIndex = float('inf')
    for index, i in enumerate(s1):
        if i not in d:
            d[i] = index
    for i in s2:
        if i in d:
            minIndex = min(minIndex, d[i])
    return -1 if minIndex == float('inf') else minIndex

print(minimumIndexedCharacterWithDict(s1, s2))