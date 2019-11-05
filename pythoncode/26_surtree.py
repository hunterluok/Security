

from pythoncode.binarytree import BinaryTree
from pythoncode.Auntil import PrintNode


class Judgesubtree:
    def equal(self, data1, data2):
        if abs(data1 - data2) < 0.00001:
            return True
        else:
            return False

    def jude(self, tree1, tree2):
        if tree2 is None:
            return True
        if tree1 is None:
            return False

        flag = False
        if self.equal(tree1.data, tree2.data):
            flag = self.compare(tree1, tree2)
        # 如果 没有找到则进行下一步的寻找，否则 就可以停止了。
        if not flag:
            flag = self.jude(tree1.left, tree2)
        if not flag:
            flag = self.jude(tree1.right, tree2)
        return flag

    def compare(self, node1, node2):
        if node2 is None:
            return True
        if node1 is None:
            return False
        if self.equal(node1.data, node2.data):
            return self.compare(node1.left, node2.left) & self.compare(node1.right, node2.right)
        else:
            return False


if __name__ == "__main__":
    bt = BinaryTree()
    bt.insertdata(8)
    bt.insertdata(4)
    bt.insertdata(12)
    bt.insertdata(2)
    bt.insertdata(6)
    bt.insertdata(14)
    bt.insertdata(16)
    bt.insertdata(13)
    bt.insertdata(19)

    bt1 = BinaryTree()
    bt1.insertdata(4)
    bt1.insertdata(2)
    bt1.insertdata(6)

    PrintNode.printnode_mid(bt.head)
    print("---" * 20)
    PrintNode.printnode_layer(bt.head)
    print("---" * 20)
    PrintNode.printnode_z(bt.head)
    print("*" * 20)
    print(Judgesubtree().jude(bt.head, bt1.head))
