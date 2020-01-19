

# 5福

def counts(data):
    count = [0] * 5
    for line in data:
        for i in range(5):
            if line[i] == '1':
                count[i] += 1
    print(count)
    return min(count)


data = ['11001','00110', '11111','00000', '00110']
print(counts(data))