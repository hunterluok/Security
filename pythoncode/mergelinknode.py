

from pythoncode import listnode


class MergeNode:
    def __init__(self):
        pass

    def merge(self, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        merged = None
        if node1.value < node2.value:
            merged = node1
            merged.nexts = self.merge(node1.nexts, node2)
        else:
            merged = node2
            merged.nexts = self.merge(node1, node2.nexts)
        return merged

    @staticmethod
    def print_value(node):
        temp = node
        while temp is not None:
            print(temp.value)
            temp = temp.nexts

class MergeNodeTherr(MergeNode):
    def __init__(self):
        super(MergeNodeTherr, self).__init__()

    def mergethree(self, node1, node2, node3):
        merged = self.merge(node1, node2)
        last = self.merge(merged, node3)
        return last


if __name__ == "__main__":
    first = listnode.ListNode()
    second = listnode.ListNode()
    third = listnode.ListNode()

    for i in range(17):
        if i % 3 == 0:
            first.push(i)
        elif i % 3 == 1:
            second.push(i)
        else:
            third.push(i)

    first.print_value()
    second.print_value()
    third.print_value()
    print("--" * 10)
    my = MergeNodeTherr()
    result = my.mergethree(first.head, second.head, third.head)
    my.print_value(result)

