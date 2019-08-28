
import numpy as np


class HashTable:
    """
    连接表法
    """
    def __init__(self, lens=20):
        self.hashlist = {}
        self.count = 0
        self.lens = lens

    def hash_fun(self, value):
        hash_address = value % self.lens
        return hash_address

    def insetdata(self, data):
        if self.count >= self.lens:
            raise ValueError("hash table is full")
        address = self.hash_fun(data)
        self.hashlist.setdefault(address, []).append(data)
        self.count += 1
        print("ok")

    def finddata(self, data):
        add = self.hash_fun(data)
        if add in self.hashlist.keys():
            if data in self.hashlist[add]:
                return "find"
            else:
                # self.insetdata(data)
                return "add, not find"
        else:
            # self.insetdata(data)
            return "not find"


class Hashgg(HashTable):
    """
    公共溢出区法
    """
    def __init__(self):
        super(Hashgg, self).__init__()
        # 地址冲突的当道 公共的set中。
        self.gglist = set()

    def insetdata(self, data):
        address = self.hash_fun(data)
        if address not in self.hashlist.keys():
            self.hashlist.setdefault(address, data)
            print("insert in the dicts")
        # 正确代码 如果重复则不加入
        elif self.hashlist[address] == data:
            print("data is same")
        # 冲突 则放入到 公共的溢出区
        else:
            self.gglist.add(data)
            print("insert in the gglist")

    def finddata(self, data):
        address = self.hash_fun(data)
        if self.hashlist[address] == data:
            return "find, in dicts"
        elif data in self.gglist:
            return "find, in gglist"
        else:
            return "not find"


class HashLine(HashTable):
    def __init__(self, lens=10):
        super(HashLine).__init__()
        self.hashlist = np.zeros(lens)
        self.lens = lens

    def insetdata(self, data):
        address = self.hash_fun(data)
        if self.hashlist[address] == 0:
            self.hashlist[address] = data
            print("ok insert")
            return
        # 这段代码其实是没有意义的
        # elif self.hashlist[address] == data:
        #    print(" value is same")
        #    return

        count = 0
        temp = address
        temp_data = data
        while self.hashlist[temp] != 0:
            temp_data = temp_data + 1
            temp = self.hash_fun(temp_data)
            print(temp, " -- temp", address)
            if temp == address:
                print("tabel is full")
                break

            count += 1
            if count > 20:
                break
        self.hashlist[temp] = data
        print("ok, line insert")
        return


if __name__ == "__main__":
    #my = HashTable()
    my = Hashgg()
    my.insetdata(1)
    my.insetdata(32)
    my.insetdata(2)
    my.insetdata(13)
    my.insetdata(12)
    my.insetdata(32)
    print(my.finddata(112))

    my2 = HashLine(10)

    my2.insetdata(1)
    my2.insetdata(11)
    my2.insetdata(2)
    my2.insetdata(11)
