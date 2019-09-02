

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


if __name__ == "__main__":
    list = [1,2, 3, 2, 2, 1, 3]
    lens = 7
    my = Gift()
    result = my.getValue(list, 7)
    print(result)
