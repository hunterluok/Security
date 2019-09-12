

from pythoncode.node import SingleNode


class ListNode:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, value):
        new_node = SingleNode(value)
        if self.head is None:
            self.head = new_node
            self.count += 1
            return
        temp = self.head
        if temp.nexts is not None:
            temp = temp.nexts
        temp.nexts = new_node
        self.count += 1

    def pop(self):
        """
        pop 掉第一个节点
        :return:
        """
        if self.head is not None:
            pop_value = self.head.value
            self.head = self.head.nexts
            self.count -= 1
            return pop_value
        else:
            print("listnode is empty")
            return None

    def print_value(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.nexts


if __name__ == "__main__":
    my = ListNode()
    my.push(1)
    my.push(2)
    my.push(3)
    my.print_value()
    my.pop()
    my.print_value()