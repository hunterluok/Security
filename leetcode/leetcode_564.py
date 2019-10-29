

class F:
    ## 如何处理负数的情况，是一个挑战。
    def get_reur(self, data):
        lens = len(data)
        mids = lens // 2
        recr = [i for i in data]
        if lens % 2 != 0:
            for ind in range(mids + 1, lens):
                recr[ind] = data[lens - ind - 1]
        else:
            for ind in range(mids, lens):
                recr[ind] = data[lens - ind - 1]
        recr = ''.join(recr)
        return recr, mids

    def sol(self, data):
        if data == '0':
            return data
        recr, pows = self.get_reur(data)
        diff_value = int(recr) - int(data)

        # 获取周边的回文数 - 大的
        high = str(int(data) + 10 ** pows)
        high_recr, _ = self.get_reur(high)
        high_diff = int(high_recr) - int(data)

        # 获取周边的回文数 - 小的
        lower = str(int(data) - 10 ** pows)
        if len(lower) < len(data):
            lower_recr = '9' * len(lower)
        else:
            lower_recr, _ = self.get_reur(lower)
        lower_diff = int(data) - int(lower_recr)

        print("recr {}, high {}, low {}".format(recr, high_recr, lower_recr))
        if diff_value == 0:
            if high_diff >= lower_diff:
                return lower_recr
            else:
                return high_recr
        elif diff_value > 0:
            if diff_value >= lower_diff:
                return lower_recr
            else:
                return recr
        else:
            # 这里需要注意的地方。
            if abs(diff_value) <= high_diff:
                return recr
            else:
                return high_recr

    # def solu(self, data):
    #     if data == '0':
    #         return data
    #     recr, mids = self.get_reur(data)
    #     diff_value = int(recr) - int(data)
    #     pows = mids
    #
    #     if diff_value > 0:
    #         lower = str(int(data) - 10 ** pows)
    #         if len(lower) < len(data):
    #             lower_recr = '9' * len(lower)
    #         else:
    #             lower_recr, _ = self.get_reur(lower)
    #         second_diff_value = int(data) - int(lower_recr)
    #         if second_diff_value <= diff_value:
    #             return lower_recr
    #         else:
    #             return recr
    #     elif diff_value < 0:
    #         high = str(int(data) + 10 ** pows)
    #         high_recr, _ = self.get_reur(high)
    #         second_diff_value = int(data) - int(high_recr)
    #
    #         if second_diff_value < diff_value:
    #             return recr
    #         else:
    #             return high_recr
    #     else:
    #         high = str(int(data) + 10 ** pows)
    #         high_recr, _ = self.get_reur(high)
    #         high_diff = int(high_recr) - int(data)
    #
    #         lower = str(int(data) - 10 ** pows)
    #         if len(lower) < len(data):
    #             lower_recr = '9' * len(lower)
    #         else:
    #             lower_recr, _ = self.get_reur(lower)
    #
    #         lower_diff = int(data) - int(lower_recr)
    #
    #         if lower_diff <= high_diff:
    #             return lower_recr
    #         else:
    #             return high_recr


if __name__ == "__main__":
    my = F()
    print(my.sol("899"))


    #print(my.solu(""))

