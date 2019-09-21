

from pythoncode import binarytree


class CoverTree:
    def __init__(self):
        self.right_node = None
        # pass

    def convt_tree(self, node):
        self.convert(node, self.right_node)
        temp = self.right_node
        while temp is not None and temp.left is not None:
            temp = temp.left
        return temp
        #return self.right_node

    def convert(self, node, right_node):
        if node is None:
            return None

        temp = node
        if temp.left is not None:
            self.convert(temp.left, right_node)

        temp.left = right_node
        if right_node is not None:
            right_node.left = temp

        right_node = temp

        if temp.right is not None:
            self.convert(node.right, right_node)
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

