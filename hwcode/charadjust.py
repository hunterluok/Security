

strs = "eeefgghhh"


di = {}
for i in strs:
    di.setdefault(i, 0)
    di[i] += 1


keys = sorted(di.keys())
maxs = max(di.values())
s = ''
for i in range(maxs):
    for k in keys:
        if di[k] != 0:
            s += k
            di[k] -= 1
        else:
            continue
print(s)

