

from pythoncode.listnode import ListNode
from pythoncode.node import SingleNode
from pythoncode.Auntil import Utils


class ListSum:
    def __init__(self):
        pass

    def listsum(self, temp1, temp2):
        new_node = None
        flag = 0

        while temp1 is not None or temp2 is not None:
            if temp1 is not None and temp2 is not None:
                newvalue = temp1.value + temp2.value
                temp1 = temp1.nexts
                temp2 = temp2.nexts
            elif temp2 is not None:
                newvalue = temp2.value
                temp2 = temp2.nexts
            else:
                newvalue = temp1.value
                temp1 = temp1.nexts

            if flag == 1:
                newvalue += 1
            if newvalue >= 10:
                flag = 1
            else:
                flag = 0
            temp_node = SingleNode(newvalue % 10)
            temp_node.nexts = new_node
            new_node = temp_node

        if flag == 1:
            temp_node = SingleNode(flag)
            temp_node.nexts = new_node
            new_node = temp_node

        return new_node


if __name__ == "__main__":
    my1 = ListNode()
    for _ in range(0, 3):
        my1.push(5)

    my2 = ListNode()
    for i in range(0, 3):
        my2.push(9)
    #my1.print_value()
    #print("**"*10)
    #my1.print_node(my1.head)
    mylist = ListSum()
    mynode = mylist.listsum(my1.head, my2.head)
    Utils.print_node(mynode)

