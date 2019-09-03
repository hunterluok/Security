
from pythoncode.node import ThreeNode


class MyNode:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, data):
        new_node = ThreeNode(data)
        if self.head is None:
            self.head = new_node
            self.count += 1
            return

        temp = self.head
        while temp is not None:
            cur = temp
            if data < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        if data < cur.value:
            cur.left = new_node
            new_node.father = cur
        else:
            cur.right = new_node
            new_node.father = cur
        self.count += 1
        return

    @classmethod
    def print_value(cls, node, lists=[]):
        """
        可以把一组数发放入到一个2叉树中， 然后中序遍历，这样就是从小到大排列了
        :param node:
        :return:
        """
        if node.left is not None:
            cls.print_value(node.left, lists)
        if node is not None:
            print("value is {}".format(node.value))
            lists.append(node.value)
        if node.right is not None:
            cls.print_value(node.right, lists)

    @classmethod
    def find_nextnode(cls, target, node):
        if target is None:
            return None
        # 如果这个节点有 右子节点，则是右子节点的 最左边的那个节点的值。
        if target.right is not None:
            temp = target.right
            while temp.left is not None:
                temp = temp.left
            return temp.value
        # 如果 右子树为 None
        if target.right is None:
            # 头结点 是没有FATHER的
            if target.father is None:
                return None
            # 说明 他是左节点
            elif target.father.left == target:
                return target.father.value
            # 如果 节点
            #elif target.father == target.father.father.left:
            #   return target.father.value
            else:
                temp = target.father
                # 沿着 右子树向上爬行
                while temp.father is not None and temp.father.right == temp:
                    temp = temp.father
                # 判断 该节点是否为 父节点的 左子节点。
                if temp is not None and temp.father is not None and temp.father.left is not None and temp.father.left == temp:
                    return temp.father.value
                if temp.father is None:
                    return None


if __name__ == "__main__":
    mynode = MyNode()
    mynode.push(10)
    mynode.push(5)
    mynode.push(15)
    mynode.push(22)
    mynode.push(12)
    mynode.push(4)
    mynode.push(8)
    mynode.push(7)
    mynode.push(9)

    mylist = []
    mynode.print_value(mynode.head, mylist)
    # print(mylist)
    # print(mynode.head.left.right.father.father.right.value)

    #test = mynode.head.left.right.right
    # test =  mynode.head.right.right
    # test = mynode.head.right.left
    test = mynode.head
    # print(test.right.value)
    print(mynode.find_nextnode(test, mynode.head))


