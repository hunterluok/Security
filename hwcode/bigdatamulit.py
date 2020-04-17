

def multi(b, suba):
    lenb = len(b)
    suba = int(suba)
    temp = []
    flag = 0
    for sub in range(lenb-1, -1, -1):
        sub_b = int(b[sub])
        s = sub_b * suba
        if flag != 0:
            s += flag
            flag = 0
        if s > 9:
            flag = s // 10
            s %= 10
        temp.append(s)
    if flag != 0:
        temp.append(flag)
    return temp


def get_result(a, b):
    result = []
    lena = len(a)
    count = 0
    max_len = 0
    for i in range(lena-1, -1, -1):
        suba = a[i]
        temp = count * [0] + multi(b, suba)
        count += 1
        result.append(temp)
        max_len = max(max_len, len(temp))
    return result, max_len


def add(result, max_len):
    p = [0] * max_len
    for i in range(len(result)):
        temp = result[i]
        if len(temp) != max_len:
            temp = temp + [0] * (max_len - len(temp))

        flag = 0
        for i in range(max_len):
            tem_re = p[i] + temp[i]
            if flag != 0:
                tem_re += flag
                flag = 0
            if tem_re > 9:
                flag = tem_re // 10
                tem_re = tem_re % 10
            p[i] = tem_re
        if flag != 0:
            p += [flag]
    p = p[::-1]
    print(''.join([str(i) for i in p]))
    return


if __name__ == "__main__":
    b = "4324"
    a = "1232"
    result, max_len = get_result(a, b)
    add(result, max_len)

