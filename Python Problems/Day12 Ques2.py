s = "DRINKEATCODE"
oneHole = set(["A", "D", "O", "P", "Q", "R"])
twoHole = set(["B"])

count = 0
def countHoles(s, oneHole, twoHole, count):
    for i in s:
        if i in twoHole:
            count+=2
        elif i in oneHole:
            count+=1
    return count

count = countHoles(s, oneHole, twoHole, count)
print(count)