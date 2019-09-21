

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


if __name__ == "__main__":
    first = listnode.ListNode()
    second = listnode.ListNode()

    for i in range(8):
        if i % 2 == 0:
            first.push(i)
        else:
            second.push(i)

    first.print_value()
    second.print_value()
    print("--" * 10)
    my = MergeNode()
    result = my.merge(first.head, second.head)
    my.print_value(result)
