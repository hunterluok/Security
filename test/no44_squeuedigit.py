

class FindDigit:
    def __init__(self):
        pass

    def finds(self, n):
        if n < 0:
            return None
        if n == 0:
            return n

        temp_n = 1
        index = 1
        count = 1
        while temp_n < n:
            temp_count = index * 9 * count
            temp_n += temp_count
            index *= 10
            count += 1
            print("--- temp_n is {}".format(temp_n))

        old_value = temp_n - temp_count
        temp_dist = n - old_value
        print("temp_dist is ", temp_dist)

        temp_int = int(temp_dist / (count - 1))
        index_value = int(temp_dist % (count - 1))
        digit = int(index / 10 + temp_int)
        print("digit is {}, index_value is {}".format(digit, index_value))
        return str(digit)[index_value]


if __name__ == "__main__":
    n = 15
    my = FindDigit()
    print(my.finds(n)) 
