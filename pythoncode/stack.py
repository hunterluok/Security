

from pythoncode.node import SingleNode


class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, value):
        self.head = SingleNode(value, nexts=self.head)
        self.count += 1

    def pop(self):
        pop_data = self.head.value
        self.head = self.head.nexts
        self.count -= 1
        return pop_data

    def show(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.nexts

    def _top(self):
        if self.head is None:
            return -1
        else:
            return self.head.value

    @property
    def stack(self):
        return self.head

    @property
    def lens(self):
        return self.count

    @property
    def top(self):
        return self._top()


class StackMin(Stack):
    """
    利用遍历的方式 查找最小值和最大值
    """
    def __init__(self):
        super(StackMin, self).__init__()
        self.min = 10000
        self.max = -10000

    def minvalue(self):
        temp = self.head
        while temp is not None:
            if self.min > temp.value:
                self.min = temp.value
            temp = temp.nexts
        return self.min

    def maxvalue(self):
        temp = self.head
        while temp is not None:
            if self.max < temp.value:
                self.max = temp.value
            temp = temp.nexts
        return self.max


class StackWithMin:
    """
    新建stack 保存最大值或最小值
    """
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()
        self.stack_3 = Stack()

    def push(self, value):
        self.stack_1.push(value)
        if self.stack_2.count == 0:
            self.stack_2.push(value)
        elif self.stack_2.top <= value:
            self.stack_2.push(self.stack_2.top)
        else:
            self.stack_2.push(value)

        if self.stack_3.count == 0:
            self.stack_3.push(value)
        elif self.stack_3.top <= value:
            self.stack_3.push(value)
        else:
            self.stack_3.push(self.stack_3.top)

    def pop(self):
        value = self.stack_1.pop()
        self.stack_2.pop()
        self.stack_3.pop()
        return value

    def get_min(self):
        return self.stack_2.top

    def get_max(self):
        return self.stack_3.top

    def show(self):
        temp = self.stack_1.head
        while temp is not None:
            print(temp.value)
            temp = temp.nexts

    def show_min(self):
        temp = self.stack_2.head
        while temp is not None:
            print(temp.value)
            temp = temp.nexts

    def show_max(self):
        temp = self.stack_3.head
        while temp is not None:
            print(temp.value)
            temp = temp.nexts

    @classmethod
    def show(cls, node):
        temp = node
        while temp is not None:
            print(temp.value)
            temp = temp.nexts


if __name__ == "__main__":
    #my = StackMin()
    my = StackWithMin()
    my.push(3)
    my.push(2)
    my.push(1)
    my.push(44)
    my.show()
    #print(my.minvalue())
    #print(my.maxvalue())
    print("---")
    # print(my.getmin())

    my.show_min()
    print("----")
    my.show_max()


