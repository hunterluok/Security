

class Rmove:
    def __init__(self, move_step, move_idx):
        self.m = move_step
        self.move_idx = move_idx

    def remove(self, data):
        data_len = len(data)
        if data_len < 1:
            return None
        while data_len != 1:
            self.move_idx = (self.move_idx + self.m) % data_len
            value = data[self.move_idx]
            data.remove(value)
            data_len = len(data)
            print("romove value is {}, index is {}, data_len is {}".format(value, self.move_idx, data_len))
        return data[0]

    @staticmethod
    def test(func, data, target):
        result = func(data)
        print("result is {}, target is {}".format(result, target))
        if result == target:
            print("passed")
        else:
            print("not passed")


if __name__ == "__main__":
    mr = Rmove(2, 1)
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #print(mr.remove(data))
    mr.test(mr.remove, data, target=4)
