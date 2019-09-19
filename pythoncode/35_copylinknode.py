

from pythoncode.listnode import ListNode


class CopyNode:
    def __init__(self):
        pass

    def copy_node(self, node1, node2, index=1):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        if index % 2 == 1:
            mergerd = node1
            mergerd.nexts = self.copy_node(node1.nexts, node2, index+1)
        else:
            mergerd = node2
            mergerd.nexts = self.copy_node(node1, node2.nexts, index+1)
        return mergerd

    @staticmethod
    def print_value(node):
        temp = node
        while temp is not None:
            print(temp.value)
            temp = temp.nexts


if __name__ == "__main__":
    my1 = ListNode()
    my2 = ListNode()
    # 注意这里需要生成 新的my2，尽管与my1中元素的值相同，否则出错。
    for i in range(4, 8):
        my1.push(i)
        my2.push(i)
    # my.print_value()
    cm = CopyNode()
    result = cm.copy_node(my1.head, my2.head)
    cm.print_value(result)

