
def operations(x,y,p,q):
    myQ = [(x,0)]
    while myQ:
        num,count = myQ.pop(0)
        if num > y:
            continue
        if num == y:
            return count
        myQ.append((num * p, count + 1))
        myQ.append((num * q, count + 1))
    return -1
            
        
x,y,p,q = 12, 2592, 2, 3
ans = operations(x,y,p,q)
print(ans)
    
