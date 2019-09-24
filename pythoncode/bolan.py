

class BoLan:
    def __init__(self):
        self.ops = ['+', '-', '*', '/']

    def cal_bolan(self, data):
        mylist = []
        for ele in data:
            if ele in self.ops:
                try:
                    # 这个地方的顺序比较重要的
                    temp2 = mylist.pop()
                    temp1 = mylist.pop()
                    if ele == '+':
                        result = int(temp1) + int(temp2)
                    elif ele == '-':
                        result = int(temp1) - int(temp2)
                    elif ele == '*':
                        result = int(temp1) * int(temp2)
                    else:
                        result = int(temp1) / int(temp2)
                    mylist.append(result)
                except:
                    return "wrong"
            else:
                mylist.append(ele)
        if len(mylist) != 1:
            return "wrong"
        return mylist[0]


if __name__ == "__main__":
    # data = ['2', '1', '+', '3', '*']
    data = ['4', '+', '13', '5', '/', '+']

    my = BoLan()
    print(my.cal_bolan(data))
