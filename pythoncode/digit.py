
"""
由至少6个，至多20个字符组成。
至少包含一个小写字母，一个大写字母，和一个数字。
同一字符不能连续出现三次 (比如 "...aaa..." 是不允许的, 但是 "...aa...a..." 是可以的)。
"""


class Digit:
    def judge(self, start):
        if start.isdigit():
            return 'digit'
        elif start.isalpha():
            if start.isupper():
                return 'up'
            else:
                return 'low'
        else:
            return 'wrong'

    def solution(self, data):
        lens = len(data)
        third_count = 0
        if lens < 6:
            third_count = 6 - lens
        elif lens > 20:
            third_count = lens - 20

        set_char = set(["digit", "up", "low"])

        starts = data[0]
        result = self.judge(starts)
        digit, big_char, small_char = False, False, False

        counts = 0

        if result not in set_char:
            counts += 1
        elif result == 'digit':
            digit = True
        elif result == 'up':
            big_char = True
        else:
            small_char = True

        sums = 1
        for i in range(1, lens):
            second = data[i]
            result = self.judge(second)

            if result not in set_char:
                counts += 1
            if not digit:
                if result == 'digit':
                    digit = True
            if not big_char:
                if result == 'up':
                    big_char = True
            if not small_char:
                if result == 'low':
                    small_char = True

            if starts == second:
                sums += 1
                if sums >=3:
                    counts += 1
            else:
                starts = second
                sums = 1

        another = 0
        if not digit:
            another += 1
        if not small_char:
            another += 1
        if not big_char:
            another += 1

        if another == 0 and counts == 0 and third_count == 0:
            return 0

        if lens < 6:
            if third_count >= another:
                return third_count + counts
            else:
                return counts + another

        # COUNT
        if lens > 20:
            if third_count >= counts:
                return third_count + another
            else:
                temp = counts - third_count
                if temp >= another:
                    return counts
                else:
                    return third_count + another

        if counts >= another:
            return counts
        else:
            return another


if __name__ == "__main__":
    data = "b*"
    print("length of data {}".format(len(data)))
    my = Digit()
    print(my.solution(data))





