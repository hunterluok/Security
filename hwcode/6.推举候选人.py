
votes = [0, 1, 1, 0, 0, 1, 0]
times = [0, 5, 10, 15, 20, 25, 30]
selects = [3, 12, 25, 15, 24, 8]


def res(data):
    if sum(data) > len(data) / 2:
        return 1
    elif sum(data) == len(data) / 2:
        return data[-1]
    else:
        return 0


def find(thre, times=times, votes=votes):
    for idex, time in enumerate(times):
        if thre > time:
            continue
        elif thre == time:
            # 如果是相等的，则
            temp = votes[: idex + 1]
            return res(temp)
        else:
            temp = votes[: idex]
            return res(temp)


if __name__ == "__main__":
    for i in selects:
        print(find(i))