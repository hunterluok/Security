

class Super:
    def construct(self, data):
        lens = len(data)
        mid = lens // 2
        temp = [i for i in data]
        if lens % 2 == 0:
            for i in range(mid, lens):
                temp[i] = data[lens - i - 1]
        else:
            for i in range(mid + 1, lens):
                temp[i] = data[lens - i - 1]
        temp = ''.join(temp)
        return int(temp)

    def jude(self, data, index, lens):
        for i in range(index):
            if data[i] != data[lens-1 - i]:
                return False
        else:
            return True

    def find(self, l, h):
        start = int(l)
        end = int(h)
        result = 0

        # i = 0
        i = int(pow(start, 0.5))
        while i <= end+1:
            i_pow = i**2
            # 失败的案例
            # if i_pow < start:
            #     i += 1
            #     continue
            if i_pow > end:
                break

            temp = str(i)
            lens = len(temp)
            index = lens // 2

            temp_2 = str(i_pow)
            lens_2 = len(temp_2)
            index_2 = lens_2 // 2

            if self.jude(temp, index, lens):
                if self.jude(temp_2, index_2, lens_2):
                    print("hw {}".format(temp_2))
                    result += 1
                # 这个地方时一个核心思想。构造下一个回文数
                nexts = str(i + pow(10, index))
                next_hw = self.construct(nexts)
            else:
                # 不是回文数 就构造他的回文数。
                next_hw = self.construct(temp)
                # 如果回文数反而变小了，则 构造新的回文数。
                if next_hw < i:
                    nexts = str(i + pow(index, 2))
                    next_hw = self.construct(nexts)
            i = next_hw
        return result


if __name__ == "__main__":
    import time
    start = time.time()
    my = Super()
    first = "116572378028741"
    second = "999999999999999999"
    print(my.find(first, second))
    # print(my.find(str(11695), str(23815)))
    print(time.time() - start)

    #print(my.jude('101',3))
    #print(my.construct("2312000990")) #, 8)