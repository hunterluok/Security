
import sys
import os

"""
parentPath = os.path.abspath("../../")
if parentPath not in sys.path:
    print(parentPath)
    sys.path.insert(0, parentPath)
"""


from pythoncode.node import SingleNode
import copy


class LinkList:
    def __init__(self):
        self.count = 0
        self.head = None

    def push(self, data):
        new_node = SingleNode(data)
        if self.head is None:
            self.head = new_node
            self.count += 1
            print("insert head")
            return

        temp = self.head
        while temp.nexts is not None:
            temp = temp.nexts
        temp.nexts = new_node
        self.count += 1
        print("insert one")
        return

    @classmethod
    def flip(cls, node):
        temp = node
        new_node = None
        while temp is not None:
            # cur = temp , 这里的copy比较重要，因为修改的了 链表的结构。
            #cur = copy.copy(temp)
            cur = temp
            temp = temp.nexts
            # 上面这句的 顺序不能换， 否则有问题
            cur.nexts = new_node
            new_node = cur
        return new_node

    @classmethod
    def flip2(cls, node):
        # 从第2个开始 翻转链表
        if node is None or node.nexts is None:
            return node
        new_node = node
        temp = node.nexts
        temp_new = None
        while temp is not None:
            cur = copy.copy(temp)
            #cur = temp
            temp = temp.nexts
            cur.nexts = temp_new
            temp_new = cur
        new_node.nexts = temp_new
        return new_node

    @staticmethod
    def check(temp_node, values):
        node = temp_node
        while node is not None:
            if node.value == values:
                return True
            node = node.nexts
        return False

    @classmethod
    def omit_k(cls, temp_node, value):
        node = temp_node
        if not LinkList.check(node, value):
            print("value is not in the nodes")
            return
        if node.value == value:
            node = node.nexts
            return node

        while node.nexts is not None:
            if node.nexts.value == value:
                node.nexts = node.nexts.nexts
                return temp_node
            node = node.nexts
        # check valu in node

    @classmethod
    def find_k(cls, node, k):
        if k == 0:
            return None
        temp_1 = copy.copy(node)
        temp_2 = copy.copy(node)
        count = 0
        while temp_1 is not None:
            temp_1 = temp_1.nexts
            count += 1
            if count > k:
                temp_2 = temp_2.nexts
        if count < k:
            return "not live"
        else:
            return temp_2.value

    @classmethod
    def print_value(cls, node):
        temp = node
        while temp is not None:
            print("value is ", temp.value)
            temp = temp.nexts
        return


if __name__ == "__main__":
    mylink = LinkList()
    mylink.push(1)
    mylink.push(2)
    mylink.push(3)
    mylink.push(4)
    mylink.push(5)
    mylink.push(6)
    mylink.print_value(mylink.head)
    print("*"*20)

    # 链表反转
    newnode = mylink.flip(mylink.head)
    mylink.print_value(newnode)
    print("*" * 20)

    # newnode = mylink.flip2(mylink.head)
    # mylink.print_value(newnode)
    #
    # print("删除*" * 20)
    # res = mylink.omit_k(mylink.head, 6)
    # mylink.print_value(res)

    # 链表中的第 K个节点。
    # mylink.print_value(mylink.head)
    # print("-"*10)
    # print(mylink.find_k(mylink.head, 1))

