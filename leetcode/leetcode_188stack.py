class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if len(prices) < 2:
            return 0
        if k < 1:
            return 0
        mins = []
        maxs = []
        i = 0
        j = 1
        while j < len(prices):
            if prices[j - 1] > prices[j]:
                temp_sum = prices[j - 1] - prices[i]
                if temp_sum > 0:
                    mins.append(prices[i])
                    maxs.append(prices[j - 1])
                i = j
                j += 1
            else:
                j += 1
        temp_sum = prices[j - 1] - prices[i]
        if temp_sum > 0:
            mins.append(prices[i])
            maxs.append(prices[j - 1])

        diff = [i - j for i, j in zip(maxs, mins)]

        if k >= len(maxs):
            last = sum(diff)
            return last

        max_len = len(maxs)
        list_loss = [0] * (max_len - 1)

        for i in range(1, max_len):
            temp = diff[i] + diff[i - 1] - (maxs[i] - mins[i - 1])
            list_loss[i - 1] = min(temp, diff[i], diff[i - 1])

        def cal(tdiff, tmaxs, tmins):
            max_len_es = len(tmaxs)
            list_loss_es = [0] * (max_len_es - 1)
            for i in range(1, max_len_es):
                temps = tdiff[i] + tdiff[i - 1] - (tmaxs[i] - tmins[i - 1])
                list_loss_es[i - 1] = min(temps, tdiff[i], tdiff[i - 1])
            return list_loss_es

        while len(maxs) != k:
            least_list = [i for i in range(len(maxs) - 1) if list_loss[i] == min(list_loss)]

            t_mydiff = diff[:]
            t_mymaxs = maxs[:]
            t_mymins = mins[:]

            temp_list_loss = list_loss[:]
            loss = float("inf")
            for index in least_list:
                mydiff = diff[:]
                mymaxs = maxs[:]
                mymins = mins[:]
                temp = mydiff[index + 1] + mydiff[index] - (mymaxs[index + 1] - mymins[index])

                if temp <= mydiff[index] and temp <= mydiff[index + 1]:
                    print("cross merge", index)
                    mymins[index + 1] = mymins[index]
                    myloss = temp

                elif mydiff[index + 1] <= temp and mydiff[index + 1] <= mydiff[index]:
                    print("omit back merge", index)
                    mymaxs[index + 1] = mymaxs[index]
                    mymins[index + 1] = mymins[index]
                    myloss = mydiff[index + 1]
                else:
                    print("omit front mergge", index)
                    myloss = mydiff[index]

                if myloss < loss:
                    t_mymaxs = mymaxs[:index] + mymaxs[index + 1:]
                    t_mymins = mymins[:index] + mymins[index + 1:]
                    t_mydiff = [i - j for i, j in zip(t_mymaxs, t_mymins)]
                    temp_list_loss = cal(t_mydiff, t_mymaxs, t_mymins)
                    loss = myloss
            print("--", t_mymaxs, t_mymins, t_mydiff)
            diff[:] = t_mydiff[:]
            maxs = t_mymaxs[:]
            mins = t_mymins[:]
            list_loss = temp_list_loss[:]
        return sum(diff)

class Solution1:
    def maxProfit(self, k: int, prices) -> int:
        if len(prices) <= 1:
            return 0
        if (k < len(prices) // 2) :
            dp = [[-prices[0], 0] for i in range(k+1)]
            for price in prices[1:]:
                for i in range(1, k+1):
                    dp[i] = [max(dp[i][0], dp[i-1][1]-price), max(dp[i][1], dp[i][0]+price)]
            return dp[k][1]
        else:
            dp = [-prices[0], 0]
            for price in prices[1:]:
                dp = [max(dp[0], dp[1]-price), max(dp[1], dp[0]+price)]
            return dp[1]


if __name__ == "__main__":
    # d = [2,6,8,7,8,7,9,4,1,2,4,5,8]
    #d = [3, 5, 3, 4, 1, 4, 5, 0, 7, 8, 5, 6, 9, 4, 1]
    d = [3, 2, 6, 5, 0, 3]
    d = [2, 4, 1]

    my = Solution1()
    print(my.maxProfit(k=2, prices=d))

