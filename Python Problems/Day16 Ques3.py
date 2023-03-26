arr = [16, 17, 4, 3, 5, 2]
st = []
ans = []

def usingStack(arr, st, ans):
    for i in range(len(arr)-1, -1, -1):
        curr = arr[i]
        while(st and st[-1]<curr):
            st.pop()
        if st:
            ans.append(st[-1])
        else:
            ans.append(-1)
        st.append(curr)
    ans = ans[::-1]

    leader = []
    for i in range(len(arr)):
        if ans[i] == -1: 
            leader.append(arr[i])
    return leader



def withoutUsingStack(arr, st, ans):
    max = -float('inf')
    leader = []
    for i in range(len(arr)-1, -1, -1):
        curr = arr[i]
        if curr >= max:
            leader.append(curr)
            max = curr
    return leader[::-1]
            
            
            
leader = usingStack(arr, st, ans)
leader = withoutUsingStack(arr, st, ans)
print(leader)