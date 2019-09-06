

a = "[s2[x][y]]"
#

class mysolue:
    def __init__(self):
        pass

    def comp(self, s):
        try:
            if isinstance(int(s), int):
                return True
        except:
            return False

    def find(self, strings):
        # 2[sss]
        if len(strings) < 2:
            return "wrong"
        lens = len(strings)
        int_lists = []

        for i in range(lens):
            temp = strings[i]
            if temp != "]":
                int_lists.append(temp)
            else:
                temp_str = int_lists.pop()

                sub_str = ""
                while temp_str != "[":
                    # 这里注意 pop 是从后往前 弹出的
                    sub_str = temp_str + sub_str
                    if len(int_lists) > 0:
                        temp_str = int_lists.pop()
                    else:
                        print("wrong")
                        break
                print("sub_str is {}".format(sub_str))

                sub_int = ""
                if len(int_lists) > 0:
                    temp_int = int_lists.pop()
                    while self.comp(temp_int):
                        sub_int = temp_int + sub_int
                        if len(int_lists) > 0:
                            temp_int = int_lists.pop()
                        else:
                            break
                    if not self.comp(temp_int):
                        int_lists.append(temp_int)

                if len(sub_int) == 0:
                    sub_int = 1
                else:
                    sub_int = int(sub_int)

                result = sub_int * sub_str
                int_lists.append(result)
                print(result, "mid result")
            print("int_list is {}".format(int_lists))
        if len(int_lists) > 1:
            return "wrong, more operation"
        return int_lists[-1]


def test(a, target):
    result = my.find(a)
    print("test result is {}".format(result))
    if result == target:
        print("passed")
        return
    else:
        print("not passed")
        return

if __name__ == "__main__":
    my = mysolue()
    #
    a = "[[z]3[s]]"
    #results = my.find(a)
    #print(results)
    #test("[[z]3[s]]", 'zsss')
    #test("10[2[z]]", 10 * "zz")

    test("[2[2[sz]]]]", 2 * 'sz')

