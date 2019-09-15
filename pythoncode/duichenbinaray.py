

from collections import deque


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
        self.myqueue = deque()
        self.mylist = []

    def compare(self, node1, node2):
        """
        判断一棵二叉树是否是对称的。
        :param node1:
        :param node2:
        :return:
        """
        if node1 is None and node2 is None:
            return True
        # 结构 是否对称进行检验
        if node1 is None or node2 is None:
            return False
        # 结构相同，但是取值 是否相同，进行判断。
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

    def width_print(self, node):
        """
        利用一个 队列， 实现广度优先遍历。
        :param node:
        :return:
        """
        if node is None:
            return
        self.myqueue.append(node)
        while len(self.myqueue) > 0:
            pop_front = self.myqueue.popleft()
            print(pop_front.data)
            if pop_front.left is not None:
                self.myqueue.append(pop_front.left)
            if pop_front.right is not None:
                self.myqueue.append(pop_front.right)

    def width_print_another(self, node):
        if node is None:
            return
        self.mylist.append(node)
        while len(self.mylist) > 0:
            first_node = self.mylist[0]
            print(first_node.data, end=" ")
            self.mylist = self.mylist[1:]
            if first_node.left is not None:
                self.mylist.append(first_node.left)
            if first_node.right is not None:
                self.mylist.append(first_node.right)


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

    print("--" * 10)
    # 判断二叉树 是否是对称的。
    my2 = MiorrTree()
    print(my2.compare(mytree, mytree))

    # 获取 镜像
    mytree2 = BniaryTree()
    for ele in [8, 6, 10, 5, 7, 9, 11]:
        mytree2.insertdata(ele)
    mytree2.print_values(mytree2.head)
    print("-*-" * 10)
    import copy
    #print("<"*4)
    # my.print_tree(mytree2.head)
    #print("镜像")
    #result = copy.copy(mytree2.head)
    #ne =
    #my2.get_mirror(mytree2.head)
    #print(my.print_tree(ne))
    #my2.get_mirror(mytree2.head)
    #print("origin al : ")
    #my.print_tree(mytree2.head)
    print("width print :")
    my2.width_print(mytree2.head)

    print("width print _list : ")
    my2.width_print_another(mytree2.head)


    a = deque()
    a.append(2)
    a.append(10)
    a.append(101)
    #print(a.pop())
    #print(a.popleft())
    # print(a.pop())
    #print(len(a))
    b = []
    print("xx is {}".format(len(b)))

