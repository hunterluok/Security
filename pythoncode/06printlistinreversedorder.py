

from pythoncode.listnode import ListNode
from pythoncode.stack import Stack


class ReversedPrint:
    def __init__(self):
        self.mystack = Stack()

    def reveseprint(self, node):
        # 利用递归的思想取解决这个问题
        if node is not None:
            if node.nexts is not None:
                self.reveseprint(node.nexts)
            print(node.value)

    def reverse(self, node):
        while node is not None:
            self.mystack.push(node)
            node = node.nexts

        while self.mystack.count > 0:
            pop_node = self.mystack.pop()
            print(pop_node.value)


if __name__ == "__main__":
    my = ListNode()
    for i in range(5):
        my.push(i)

    my2 = ReversedPrint()
    # my2.reveseprint(my.head)
    # my.head 才是链接表， 这与数据结构有关。
    my2.reverse(my.head)