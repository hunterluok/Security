

from pythoncode.binarytree import BniaryTree


class PathInTree:
    def __init__(self, target=None):
        self.path = []
        self.sums = 0
        self.target = target
        self.last_path = None

    def find_path(self, node):
        # if node is None:
        #     return
        self.sums += node.data
        self.path.append(node.data)

        left = (node.left is None) & (node.right is None)
        if left and self.sums == self.target:
            print("find the path")
            for i in self.path:
                print(i, end=" ")
            self.last_path = self.path[:]
            print("\n")

        if node.left is not None:
            self.find_path(node.left)
        if node.right is not None:
            self.find_path(node.right)
        # 最终一场空
        self.sums -= node.data
        self.path.pop()

    @property
    def get_path(self):
        return self.last_path


if __name__ == "__main__":
    bt = BniaryTree()
    bt.insertdata(8)
    bt.insertdata(4)
    bt.insertdata(12)
    bt.insertdata(2)
    bt.insertdata(6)
    bt.insertdata(10)
    bt.insertdata(14)

    bt.insertdata(1)
    bt.insertdata(3)
    bt.insertdata(5)
    bt.insertdata(7)
    bt.insertdata(9)
    bt.insertdata(11)
    bt.insertdata(13)
    bt.insertdata(15)
    print("*" * 10)
    bt.print_node_level(bt.head)
    print("--" * 10)
    my = PathInTree(target=223)
    my.find_path(bt.head)

    print(my.get_path)

