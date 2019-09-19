

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
        else:
            temp = self.head
            # 这里的 while 而不是 if 一定要注意的
            while temp.nexts is not None:
                temp = temp.nexts
            temp.nexts = new_node
            self.count += 1
            return

    def push_node(self, mynode):
        if self.head is None:
            self.head = mynode
            self.count += 1
            return
        temp = self.head
        while temp.nexts is not None:
            temp = temp.nexts
        temp.nexts = mynode
        self.count += 1
        return

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

    @property
    def younode(self):
        return self.head


if __name__ == "__main__":
    my = ListNode()
    for i in range(4, 8):
        my.push(i)

    my.print_value()