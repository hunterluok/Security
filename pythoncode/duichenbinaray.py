

from pythoncode.binarytree import BniaryTree
from pythoncode.node import BinaryTreeNode


class MyBinaryTree(BniaryTree):
    def __init__(self):
        super(MyBinaryTree, self).__init__()
        self.head = None
        self.count = 0

    def push(self, node):
        """
        继承重写了部分代码， 修改了push的形式，原始是value,现在是 node
        :param node:
        :return:
        """
        if self.head is None:
            self.head = node
            self.count += 1
            return

        temp = self.head
        new_value = node.data
        while temp is not None:
            cur = temp
            if new_value < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        if new_value < cur.data:
            cur.left = node
        else:
            cur.right = node
        self.count += 1

    @classmethod
    def print_tree(cls, tree):
        if tree.left is not None:
            cls.print_tree(tree.left)
        # 中序遍历
        if tree is not None:
            print(tree.data)
        if tree.right is not None:
            cls.print_tree(tree.right)


mytree = BinaryTreeNode(data=8)
mytree.left = BinaryTreeNode(data=6)
mytree.right = BinaryTreeNode(data=6)

mytree.left.left = BinaryTreeNode(data=5)
mytree.left.right = BinaryTreeNode(data=7)
mytree.right.left = BinaryTreeNode(data=7)
mytree.right.right = BinaryTreeNode(data=5)


class MiorrTree:
    def __init__(self):
        pass

    def compare(self, node1, node2):
        """
        判断一棵二叉树是否是对称的。
        :param node1:
        :param node2:
        :return:
        """
        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False

        if node1.data != node2.data:
            return False
        # 如果相等的化 进行下一步的比较，就行了的。
        # 这里需要注意，同时满足 左边和右边同时相等。
        return self.compare(node1.left, node2.right) and self.compare(node1.right, node2.left)

    def get_mirror(self, node):
        """
        获取树的镜像
        :param node:
        :return:
        """
        if node is None:
            return
        if node.right is None and node.left is None:
            return

        #temp = node.right
        #node.right = node.left
        #node.left = temp
        # 这么写 更简洁
        node.right, node.left = node.left, node.right

        if node.left is not None:
            self.get_mirror(node.left)
        if node.right is not None:
            self.get_mirror(node.right)
        # 这是是否 进行 return 都是可以的，但是 原始的 node 肯定会被修改了。
        # return node


if __name__ == "__main__":
    my = MyBinaryTree()
    for i in [6, 4, 2, 7, 11, 9]:
        node = BinaryTreeNode(i)
        my.push(node)
    mylists = []
    my.print_values_anther(my.head, mylists)
    print("*" * 20)
    print(mylists)
    my.print_tree(mytree)

    print("--"*10)
    # 判断二叉树 是否是对称的。
    my2 = MiorrTree()
    print(my2.compare(mytree, mytree))

    # 获取 镜像
    mytree2 = BniaryTree()
    for ele in [8, 6, 10, 5, 7, 9, 11]:
        mytree2.insertdata(ele)
    mytree2.print_values(mytree2.head)


    import copy
    print("<"*4)
    my.print_tree(mytree2.head)
    print("镜像")
    #result = copy.copy(mytree2.head)
    #ne =
    my2.get_mirror(mytree2.head)
    #print(my.print_tree(ne))

    #my2.get_mirror(mytree2.head)
    print("origin al : ")
    my.print_tree(mytree2.head)


