

class UglyNumber:
    def __init__(self):
        pass

    def judge(self, temp_data):
        # 判断是否为满足添加的 丑数。
        while temp_data % 2 == 0:
            temp_data /= 2
        while temp_data % 3 == 0:
            temp_data /= 3
        while temp_data % 5 == 0:
            temp_data /= 5

        if temp_data == 1:
            return True
        else:
            return False


    def get(self, n):
        if n < 1:
            return "wrong"

        temp = 0
        count = 0
        # 从0开始的化，就是count < n;
        while count < n:
            temp += 1
            if self.judge(temp):
                count += 1
                print("counts is {}, ugly number is {}".format(count, temp))
        return temp


if __name__ == "__main__":
    my = UglyNumber()
    print(my.get(20))