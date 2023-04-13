import re
pattern = '^a...f$'
string = 'abcdf'
result = re.match(pattern, string)
if result:
    print("Match")
else:
    print("No match")