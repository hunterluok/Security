

class SaiZi:
    def __init__(self, n):
        self.n = n
        self.dicts = {}
        pass

    def cal(self, m):
        if m < 1 or self.n < 1:
            return "wrong"

        self.dicts = {k: 1 for k in range(1, 7)}
        index = 2
        while index <= m:
            old_key = set(self.dicts.keys())
            # print("old_key is {}".format(old_key))
            new_dict = {}
            for j in range(1, self.n+1):
                for key in old_key:
                    #print(" pair is {}-{}".format(j, key))
                    temp = j + key
                    # print("temp is {}".format(temp))
                    new_dict.setdefault(temp, 0)
                    new_dict[temp] += 1
            self.dicts = new_dict
            index += 1
        #result = {k:v/valus for k, v in self.dicts.items()}
        print("result len is {}".format(len(self.dicts)))
        return self.dicts #result


if __name__ == "__main__":
    my = SaiZi(6)
    result = my.cal(4)
    print(result)