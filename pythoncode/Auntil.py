
from pythoncode.binarytree import BinaryTree


class Utils:
    @staticmethod
    def print_node(node):
        while node is not None:
            print(node.value, end='')
            node = node.nexts

    def passes(self):
        pass


class PrintNode:
    @classmethod
    def printnode_mid(cls, node):
        if node is not None:
            print(node.data, end=" ")
        if node.left is not None:
            cls.printnode_mid(node.left)
        if node.right is not None:
            cls.printnode_mid(node.right)

    @staticmethod
    def printnode_z(node):
        if node is None:
            return None
        node_list = []
        node_list.append(node)
        count = 1
        flag = 1

        print_flag = True
        temp_list = []

        while len(node_list) != 0:
            temp_node = node_list[0]
            node_list = node_list[1:]
            count -= 1
            flag -= 1
            temp_list.append(temp_node)

            if temp_node.left is not None:
                node_list.append(temp_node.left)
                flag += 1
            if temp_node.right is not None:
                node_list.append(temp_node.right)
                flag += 1

            if count == 0:
                if print_flag:
                    print_flag = False
                else:
                    temp_list = temp_list[::-1]
                    print_flag = True
                for temp_node in temp_list:
                    print(temp_node.data, end=" ")

                print("\n")
                temp_list = []
                count = flag


    @staticmethod
    def printnode_layer(node):
        if node is None:
            return None

        lists = []
        lists.append(node)
        count = 1
        flag = 1

        while len(lists) != 0:
            temp_node = lists[0]
            print(temp_node.data, end=" ")
            lists = lists[1:]
            count -= 1
            flag -= 1

            if temp_node.left is not None:
                lists.append(temp_node.left)
                flag += 1
            if temp_node.right is not None:
                lists.append(temp_node.right)
                flag += 1

            if count == 0:
                print("\n")
                count = flag

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
    PrintNode.printnode_mid(bt.head)
    print("---" * 20)
    PrintNode.printnode_layer(bt.head)
    print("---" * 20)
    PrintNode.printnode_z(bt.head)
