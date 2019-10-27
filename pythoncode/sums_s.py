

def solution(nsums):
    if nsums < 3:
        return []
    result = []
    mid = nsums // 2
    k = 2
    nsums2 = 2 * nsums
    while k <= mid+1:
        if nsums2 % k == 0:
            value = nsums // k
            front = (k-1) // 2
            last = k - front - 1
            if value - front < 1:
                break
            # 注意这里的 问题
            if (last - front) * k // 2 == nsums - value * k:
                print("value is {}".format(value))
                temp_list = []
                # 注意这里的 last+1 与特定的语言有关。
                for j in range(-front, last +1):
                     temp_list.append(value + j)
                result.append(temp_list)
        k += 1
    result = result[::-1]
    return result



if __name__ == "__main__":
    s = 100
    print(solution(s))
    [print(i) for i in range(9, 17)]