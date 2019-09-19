

from pythoncode.node import BinaryTreeNode as node
from collections import  deque


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

    def get_maxk(self, k):
        # 先进行 中序遍历，将结果存在列表中，然后再取第K大
        temp = self.head
        mylist = []
        self.print_values_anther(temp, mylist)
        return mylist[k-1]

    @staticmethod
    def print_zhi(node):
        if node is None:
            return

        mylist = deque()
        print_index = 1
        count_index = 0
        even_index = 0
        mylist.append(node)
        mylist_temp = deque()
        while len(mylist) > 0:
            temp_node = mylist[0]
            mylist_temp.append(temp_node)

            if temp_node.left is not None:
                mylist.append(temp_node.left)
                count_index += 1
            if temp_node.right is not None:
                mylist.append(temp_node.right)
                count_index += 1

            print_index -= 1
            mylist.popleft()

            if print_index == 0:
                if even_index == 0:
                    while len(mylist_temp) > 0:
                        pop_node = mylist_temp.popleft()
                        print(pop_node.data, end=" ")
                    even_index = 1
                elif even_index == 1:
                    while len(mylist_temp) > 0:
                        pop_node = mylist_temp.pop()
                        print(pop_node.data, end=" ")
                    even_index = 0
                print("\n")
                print_index = count_index
                count_index = 0

    @staticmethod
    def print_width(node):
        if node is None:
            return
        mylist = deque()
        mylist.append(node)
        while len(mylist) > 0:
            temp_node = mylist[0]
            print(temp_node.data)
            if temp_node.left is not None:
                mylist.append(temp_node.left)
            if temp_node.right is not None:
                mylist.append(temp_node.right)
            mylist.popleft()

    @staticmethod
    def print_node_level(node):
        """
        同一层的 节点放在一起
        :param node:
        :return:
        """
        if node is None:
            print("node is None")
            return
        node_list = []
        # 计数需要打印的节点数量
        level_index = 0
        # 标记需要 打印的 节点的数量
        print_index = 1
        node_list.append(node)
        while len(node_list) > 0:
            mynode = node_list[0]
            print(mynode.data, end=' ')
            if mynode.left is not None:
                node_list.append(mynode.left)
                level_index += 1
            if mynode.right is not None:
                node_list.append(mynode.right)
                level_index += 1

            node_list = node_list[1:]
            print_index -= 1
            if print_index == 0:
                print('\n')
                print_index = level_index
                level_index = 0

    @classmethod
    def print_values(clf, tree, k=1, target=None):
        # if tree is not None:
            #print(tree.data)
        if tree.left is not None:
            clf.print_values(tree.left, k=k+1, target=target)
        # 中序遍历
        if tree is not None:
            print(tree.data)
            # 这种方法是不行的 ，因为 左右子树 可能是并行进行的，而不是对全局的
            # if target is not None:
            #   if target == k:
            #       print(tree.data)
            #        return
        if tree.right is not None:
            clf.print_values(tree.right, k=k+1, target=target)

    @classmethod
    def print_values_anther(clf, tree, lists=None):
        #if tree is not None:
            #print(tree.data)
        if tree.left is not None:
            clf.print_values_anther(tree.left, lists)
        # 中序遍历
        if tree is not None:
            print(tree.data)
            if lists is not None:
                lists.append(tree.data)
        if tree.right is not None:
            clf.print_values_anther(tree.right, lists)
        #if tree.left is not None:
         #   clf.print_values(tree.left)
        # 后序遍历
        #xif tree is not None:
        #    print(tree.data)

    @classmethod
    def print_nodevalue(cls, model, i=0):
        """
        如何递归的去打印子叶节点的，标号。#这里是中序遍历。
        """

        # if model.left is not None:
        #   cls.print_nodevalue(model.left, i=i+1)
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
        # 此处 两个节点之间的深度算1。
        max_deep = 1
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
    def get_deep_another(cls, tree):
        """
        此处 一层节点算 一个deep
        :param tree:
        :return:
        """
        if tree is None:
            return 0

        left_deep = cls.get_deep_another(tree.left)
        right_deep = cls.get_deep_another(tree.right)
        if left_deep > right_deep:
            max_deep = left_deep + 1
        else:
            max_deep = right_deep + 1
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
    # bt.print_values(bt.head)
    #result = \
    bt.print_values_anther(bt.head)
    print("*"*10)
    # print(bt.count, " total values")
    # print(bt.get_treedeep(bt.head))
    #print("result is {} ".format(result))
    #res= bt.get_maxk(3)
    #print("result is {} ".format(res))
    # deep = bt.get_treedeep(bt.head)
    # deep_2 = bt.get_deep_another(bt.head)
    # print("Tree deep is {} , {}".format(deep, deep_2))
    bt.print_node_level(bt.head)
    print("*" * 20)
    # bt.print_width(bt.head)
    bt.print_zhi(bt.head)
