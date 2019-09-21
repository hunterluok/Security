

from pythoncode import binarytree


class CoverTree:
    def __init__(self):
        self.right_node = None

    def convt_tree(self, node):
        self.convert(node)
        temp = self.right_node
        while temp is not None and temp.left is not None:
           temp = temp.left
        return temp

    def convert(self, node):
        """
        核心的代码
        :param node:  二叉搜索树
        :return: 无
        """
        if node is None:
            return None

        temp = node
        if temp.left is not None:
            self.convert(temp.left)

        temp.left = self.right_node
        if self.right_node is not None:
            self.right_node.right = temp

        self.right_node = temp
        if temp.right is not None:
            self.convert(temp.right)
        # return node

    @staticmethod
    def prints(node):
        while node is not None:
            print(node.data)
            node = node.right

if __name__ == "__main__":
    bt = binarytree.BniaryTree()
    bt.insertdata(8)
    bt.insertdata(4)
    bt.insertdata(12)
    bt.insertdata(2)
    bt.insertdata(6)
    bt.insertdata(10)
    bt.insertdata(14)

    bt.print_node_level(bt.head)
    print("*" * 20)

    my = CoverTree()
    result = my.convt_tree(bt.head)
    my.prints(result)

