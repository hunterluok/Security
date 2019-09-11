
"""
如何在数据中， 寻找到 众数。

"""
"""
春节期间小明使用微信收到很多个红包，非常开心。在查看领取红包记录时发现，某个红包金额出现的次数超过了红包总数的一半。
请帮小明找到该红包金额。写出具体算法思路和代码实现，要求算法尽可能高效。
给定一个红包的金额数组gifts及它的大小n，请返回所求红包的金额。
若没有金额超过总数的一半，返回0。

[1,2,3,2,2],5 返回2。
"""


class Gift:
    def getValue(self, gifts, n):
        # write code here
        count_value = []
        count_index = []
        for git in gifts:
            if git not in count_value:
                count_value.append(git)
                count_index.append(1)
            else:
                indexs = count_value.index(git)
                count_index[indexs] += 1
        maxvalue = max(count_index)
        if maxvalue > int(n / 2):
            myindex = count_index.index(maxvalue)
            mygit = count_value[myindex]
            return mygit
        else:
            return 0


class Giftnew:
    def __init__(self):
        pass

    def jude(self, data, lens, target):
        time = 0
        for i in range(lens):
            if data[i] == target:
                time += 1
        if time * 2 > lens:
            return True
        else:
            return False

    def getValue(self, data, lens):
        result = data[0]
        time = 1
        for i in range(1, lens):
            if time == 0:
                result = data[i]
                time = 1
            elif data[i] == result:
                time += 1
            else:
                time -= 1
        if time >= 1 and self.jude(data, lens, result):
            return result
        else:
            return 0



if __name__ == "__main__":
    lists = [4, 4, 4, 1, 2, 3, 4]
    # lists = [1, 2, 3, 4, 5]
    lens = len(lists)
    my = Giftnew()
    result = my.getValue(lists, lens)
    print(result)
