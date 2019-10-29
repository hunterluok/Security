class Solution:
    def judge(self, data):
        if data.isdigit():
            return "digit"
        elif data.isalpha():
            if data.isupper():
                return 'up'
            else:
                return 'low'
        else:
            return 'wrong'

    def strongPasswordChecker(self, s: str) -> int:
        lens = len(s)
        if lens < 1:
            return 6
        third_count = 0
        if lens < 6:
            third_count = 6 - lens
        if lens > 20:
            third_count = lens - 20

        digit = False
        up = False
        low = False

        starts = None
        counts = 0
        sums = 0

        for i in range(lens):
            second = s[i]
            result = self.judge(second)
            if starts == second:
                sums += 1
                if sums % 3 == 0:
                    counts += 1
            else:
                sums = 1
                starts = second

            if not digit:
                if result == 'digit':
                    digit = True
            if not up:
                if result == 'up':
                    up = True
            if not low:
                if result == 'low':
                    low = True
        another = 0
        if not digit:
            another += 1
        if not up:
            another += 1
        if not low:
            another += 1
        print("another {}, counts {}, third_count {}".format(another, counts, third_count))
        if another == 0 and counts == 0 and third_count == 0:
            return 0
        if lens < 6:
            if third_count >= another:
                temp = third_count - another
                if temp > counts:
                    return third_count
                else:
                    return counts + another
            else:
                temp = another - third_count
                if temp > counts:
                    return another
                else:
                    return counts + third_count

        # another 缺失de
        # counts 重复 需要处理的
        # 需要删除的 third_counnt
        if lens > 20:
            if another >= counts:
                print("---")
                return third_count + another
            else:
                temp = counts - another

                if third_count % 3 == 0:
                    temp_anp = third_count // 3
                else:
                    temp_anp = third_count // 3 + 1

                if temp_anp > temp:
                    print("dsd here")
                    return temp_anp + another
                else:
                    print("there")
                    return counts - temp_anp + third_count + 1

        if counts >= another:
            return counts
        else:
            return another

if __name__ == "__main__":
    data = "a11aaa12234111sdadas111"
    # data = "111111111111111111111"
    print("length of data {}".format(len(data)))
    my = Solution()
    print(my.strongPasswordChecker(data))