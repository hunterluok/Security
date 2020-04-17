
def compare(ele, data):
    for line in data:
        # print("---", line)
        if line > ele:
            return False
    return True

def print_data(data):
    while len(data) > 1:
        ele = data[0]
        data = data[1:]
        if compare(ele, data):
            print(ele)
        else:
            data.append(ele)
    print(data[0])
    return

data = list(np.random.randint(0, 11, size=7))
print(data)
print_data(data)