# 股票筛选策略

import numpy as np


class Choose:
    def __init__(self):
        pass

    def exchange(self, data, low=0.5, high=0.85, last_day=3):
        temp = []
        for line in data:
            try:
                temp.append(float(line[10]))
            except:
                pass
                # print(line)
        temp_sort = sorted(temp)
        p_high = temp_sort[int(high * len(temp))]
        p_low = temp_sort[int(low * len(temp))]
        p_now = np.mean(temp[: last_day])
        if p_now > p_low and p_now < p_high:
            print("nice stock {}".format(data[0][1]))
            return data[0][1]
            #print(low, mid_high, now)
        else:
            print("stock is not interesting")
            return None