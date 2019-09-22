

from pythoncode import  binarytree


class BalanceTree:
    def __init__(self):
        pass


    def isbance(self, node):
        pass


    def get_deep(self, node):
        if node is None:
            return 0

        left = self.get_deep(node.left)
        right = self.get_deep(node.right)
        if left > right:
            max_len = 1 + left
        else:
            max_len = 1 + right
        return max_len


if __name__ == "__main__":
    bt = binarytree.BinaryTree()
    bt.insertdata(8)
    bt.insertdata(4)
    bt.insertdata(12)
    bt.insertdata(2)
    bt.insertdata(6)
    bt.insertdata(10)
    bt.insertdata(14)

    bt.insertdata(1)
    bt.insertdata(3)



    bt.print_node_level(bt.head)
    print("*" * 20)

    my = BalanceTree()
    print(my.get_deep(bt.head))

