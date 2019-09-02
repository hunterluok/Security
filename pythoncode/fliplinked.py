
import sys
import os

"""
parentPath = os.path.abspath("../../")
if parentPath not in sys.path:
    print(parentPath)
    sys.path.insert(0, parentPath)
"""


from pythoncode.node import SingleNode


class LinkList:
    def __init__(self):
        self.count = 0
        self.head = None

    def push(self, data):
        new_node = SingleNode(data)
        if self.head is None:
            self.head = new_node
            self.count += 1
            print("insert head")
            return

        temp = self.head
        while temp.nexts is not None:
            temp = temp.nexts
        temp.nexts = new_node
        self.count += 1
        print("insert one")
        return

    @classmethod
    def flip(cls, node):
        temp = node

        new_node = None
        while temp is not None:
            cur = temp
            cur.nexts = new_node
            new_node = cur
            temp = temp.nexts
        return new_node

    @classmethod
    def print_value(cls, node):
        temp = node
        while temp is not None:
            print("value is ", temp.value)
            temp = temp.nexts
        return


if __name__ == "__main__":
    mylink = LinkList()
    mylink.push(3)
    mylink.push(2)
    mylink.push(22)
    mylink.print_value(mylink.head)
    print("*"*20)

    newnode = mylink.flip(mylink.head)
    mylink.print_value(newnode)



