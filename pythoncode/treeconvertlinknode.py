

from pythoncode import binarytree
from pythoncode.node import BinaryTreeNode
#
from pythoncode.binarytree import BinaryTree


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

    @staticmethod
    def write(node):
        with open("a.txt", "w") as f:
            CoverTree.serilize(node, f)

    @classmethod
    def serilize(cls, node, f):
        if node is None:
            s = '#,'
            f.write(s)
            return
        f.write(str(node.data) + ',')
        cls.serilize(node.left, f)
        cls.serilize(node.right, f)

    @staticmethod
    def read(path='a.txt', pattern='r'):
        with open(path, pattern) as f:
            lists = f.readline().strip(',').split(',')
            result = CoverTree.deserilize(lists)
        return result

    @classmethod
    def deserilize(cls, lists):
        # lens = len(lists)
        my = BinaryTree()
        for ele in lists:
            if ele != '#':
                my.insertdata(ele)
        return my

    @classmethod
    def print_front(cls, node):
        if node is not None:
            print(node.data, end=' ')
        if node.left is not None:
            cls.print_front(node.left)
        if node.right is not None:
            cls.print_front(node.right)

if __name__ == "__main__":
    bt = binarytree.BinaryTree()
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
    # result = my.convt_tree(bt.head)
    # my.prints(result)

    print("--"*20)
    my.write(bt.head)
    print("--"*20)

    new = my.read()
    # bt.print_node_level(new.head)
    # bt.print_width(new.head)
    my.print_front(new.head)

