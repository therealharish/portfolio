s1 = "aab"
s2 = "xxy"

s1 = "paper"
s2 = "title"

s1 = "badc"
s2 = "baba"

def isomorphicStrings(s1, s2):
    d1 = {}
    d2 = {}
    i, j = 0,0
    while(i<len(s1)):
        first, second = s1[i], s2[j]
        if first not in d1 and second not in d2:
            d1[first] = second
            d2[second] = first
        elif first in d1 and second in d2:
            if d1[first] != second:
                return False
            if d2[second] != first:
                return False
        else:
            return False
        i+=1
        j+=1
    return True

print(isomorphicStrings(s1, s2))