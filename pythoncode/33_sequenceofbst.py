

from pythoncode.binarytree import BniaryTree


class Check:
    def __init__(self):
        pass

    @classmethod
    def check(cls, list_data):
        lens = len(list_data)
        if lens < 1:
            print("wrong")
            return None
        if lens == 1:
           return True

        root = list_data[-1]
        left = 0
        while left < lens:
            if list_data[left] < root:
                left += 1
            else:
                break

        for ele in list_data[left:-1]:
            if ele < root:
                return False

        left = True
        if left > 0:
            left = cls.check(list_data[:left])
        right = True
        if lens - left > 1:
            right = cls.check(list_data[left:-1])
        return left & right



if __name__ == "__main__":
    bt = BniaryTree()
    bt.insertdata(8)
    bt.insertdata(4)
    bt.insertdata(12)
    bt.insertdata(2)
    bt.insertdata(6)
    bt.insertdata(10)
    bt.insertdata(14)

    mylist = [2, 6, 4, 10, 14, 8, 12]

    mylist = [4, 8, 6, 12, 16, 14, 10]
    mylist = [1, 2, 3, 4, 5]
    # mylist = [5, 4, 3, 2, 1]
    # mylist = [7, 4, 6, 5]
    # mylist = [4, 6, 12, 8, 16, 14, 10]
    my = Check()
    print(my.check(mylist))
