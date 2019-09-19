

from pythoncode.node import SingleNode


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push(self, value):
        new_node = SingleNode(value)
        if self.head is None:
            self.tail = new_node
            self.head = self.tail
            self.count += 1
            return
        self.tail.nexts = new_node
        self.tail = new_node
        self.count += 1
        return

    def pop(self):
        if self.head is None:
            print("node is emepty")
            return
        self.head = self.head.nexts
        self.count -= 1
        return

    def fornt(self):
        node = self.head
        return node

    def another(self):
        pass

