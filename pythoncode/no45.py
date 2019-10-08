

class Rank:
    def __init__(self):
        pass

    def ranks(self, data):
        if len(data) < 2:
            return data[0]
        lens = len(data)
        index = lens-1

        temp = str(data[index])
        while index > 0:
            index -= 1
            temp_data = str(data[index])
            temp_1 = temp + temp_data
            temp_2 = temp_data + temp
            if temp_1 > temp_2:
                temp = temp_2
            else:
                temp = temp_1
        return temp
        #return int(temp)


if __name__ == "__main__":
    my = Rank()
    print(my.ranks([44, 32, 321]))


