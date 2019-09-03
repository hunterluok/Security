

from pythoncode.node import BinaryTreeNode as node


class BniaryTree:
    def __init__(self):
        self.head = None
        self.count = 0

    def insertdata(self, value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            self.count += 1
            return
        temp = self.head
        while temp is not None:
            cur = temp
            if value < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        if value < cur.data:
            cur.left = new_node
        else:
            cur.right = new_node
        self.count += 1

    @classmethod
    def print_values(clf, tree):
        #if tree is not None:
            #print(tree.data)
        #if tree.left is not None:
         #   self.print_values(tree.left)
        # 中序遍历
        #if tree is not None:
        #    print(tree.data)
        if tree.right is not None:
            clf.print_values(tree.right)
        if tree.left is not None:
            clf.print_values(tree.left)
        # 后序遍历
        if tree is not None:
            print(tree.data)

    @classmethod
    def print_nodevalue(cls, model, i=0):
        """
        如何递归的去打印子叶节点的，标号。#这里是中序遍历。
        """

        # if model.left is not None:
        # cls.print_nodevalue(model.left, i=i+1)
        if model.value is not None:
            # print(model.value)
            print("level {}, model value is {}".format(i, model.value))
        if model.left is not None:
            cls.print_nodevalue(model.left, i=i + 1)
        if model.right is not None:
            cls.print_nodevalue(model.right, i=i + 1)

    @classmethod
    def get_treedeep(cls, tree):
        """
        计算树的最大深度
        """
        max_deep = 0
        if tree.left is not None:
            temp_deep = 1 + cls.get_treedeep(tree.left)
            if temp_deep > max_deep:
                max_deep = temp_deep
        if tree.right is not None:
            temp_deep = 1 + cls.get_treedeep((tree.right))
            if temp_deep > max_deep:
                max_deep = temp_deep
        return max_deep

    @classmethod
    def find_value(cls, model, data):
        # 没法用 RETURN
        if model.value == data:
            print("find")
        if model.left is not None:
            cls.find_value(model.left, data)
        if model.right is not None:
            cls.find_value(model.right, data)

    @property
    def allnode(self):
        return self.head


if __name__ == "__main__":
    bt = BniaryTree()
    bt.insertdata(4)
    bt.insertdata(2)
    bt.insertdata(3)
    bt.insertdata(5)
    bt.print_values(bt.head)
    print(bt.count, " total values")
    print(bt.get_treedeep(bt.head))
