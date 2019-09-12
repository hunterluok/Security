

from pythoncode.node import SingleNode

# 公共节点
gg_first = SingleNode(1000)
gg_second = SingleNode(2000)
gg_test = SingleNode(-100)


# 节点的构造
first = SingleNode(100)
first.nexts = SingleNode(200)
first.nexts.nexts = gg_first
first.nexts.nexts.nexts = gg_second


second = SingleNode(10)
second.nexts = gg_first
second.nexts.nexts =gg_second
second.nexts.nexts.nexts = gg_test
# 指针问题，first的尾节点指针 也互自动添加 gg_test


class Findnode:
    def __init__(self):
        pass

    def findfirstnode(self, node1, node2):
        #if node1.value == node2.value:
        #    # 适用于第一个头节点 就是 公共节点的情况。
        #    return "find is, value is {}".format(node1.value)
        # 一旦公共节点相遇后，后面的节点都是一样的。这是因为 指针的问题，导致的。
        diff = self.get_nodelen(node1) - self.get_nodelen(node2)
        temp1 = node1
        temp2 = node2

        if diff > 0:
            for _ in range(diff):
                temp1 = temp1.nexts
        else:
            for _ in range(abs(diff)):
                temp2 = temp2.nexts

        while temp1 is not None and temp2 is not None:
            if temp1.value == temp2.value:
                return "find is, value is {}".format(temp2.value)
            else:
                temp1 = temp1.nexts
                temp2 = temp2.nexts
        return "Don't have the node"


    @staticmethod
    def print_node(node):
        while node is not None:
            print(node.value)
            node = node.nexts

    @staticmethod
    def get_nodelen(node):
        count = 0
        while node is not None:
            count += 1
            node = node.nexts
        return count

if __name__ == "__main__":
    my = Findnode()
    my.print_node(first)
    print("*" * 20)
    my.print_node(second)
    print("*" * 20)
    print("node lens is {}".format(my.get_nodelen(first)))
    print("node lens is {}".format(my.get_nodelen(second)))
    print("*" * 10)

    print(my.findfirstnode(first, second))

