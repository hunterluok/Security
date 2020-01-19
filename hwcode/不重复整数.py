
import sys

strs = "9876673"
lens = len(strs)
data = set()
s = ''

for i in range(lens -1, -1, -1):
    if strs[i] not in data:
        s += strs[i]
        data.add(strs[i])
print(s)
