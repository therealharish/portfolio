s = input()
chars = ""
for i in s:
    if i.isalpha():
        chars += i
chars = chars[::-1]
newS = ""
j = 0
for i in s:
    if i.isalpha():
        newS += chars[j]
        j+=1
    else:
        newS += i
print(newS)      
