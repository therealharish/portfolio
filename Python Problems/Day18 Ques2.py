# valid parenthesis
def checkValidParenthesis(s):
    st = []
    for i in s:
        if i in openSet:
            st.append(i)
        else:
            if not st:
                return False
            if st[-1] != d[i]:
                return False
            else:
                st.pop()
    if st:
        return False
    return True        
    


d = {'}':'{', 
     ')':'(',
     ']':'['}

openSet = set(['{', '(', '['])
s = '()[]{}'
s = '({[]})'
s = '({}()'
print(checkValidParenthesis(s))