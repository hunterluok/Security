
# data = [-30, -20, -10, 10, -5, 20]
data = [-28, 81, -20, 28, -29]
k = 89
lens = len(data)
sums = data[0]
start = 0

for i in range(1, lens):
    temp = data[i]
    if sums < 0:
        if temp > sums:
            sums = temp
            start = i
        else:
            start = i
            print(i - start)
    else:
        sums += temp

print(sums)
