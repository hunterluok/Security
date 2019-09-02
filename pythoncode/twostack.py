

class node:
    def __init__(self, value=None, nexts=None):
        self.value = value
        self.nexts = nexts


class Stack:
    def __init__(self):
        self.head = None
        self.counts = 0

    def push(self, value):
        """

        :param value: 插入栈的值
        :return:
        """
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            self.counts += 1
            print("ok insert")
            return

        new_node.nexts = self.head
        self.head = new_node
        self.counts += 1
        print("ok insert")
        return

    def pop(self):
        temp = self.head
        if temp is not None:
            popvalue = temp.value
            self.head = self.head.nexts
            self.counts -= 1
            return popvalue

    def print_values(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.nexts

    @property
    def length(self):
        return self.counts


class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, value):
        self.stack1.push(value)

    def pop(self):
        if self.stack1.length == 0 and self.stack2.length == 0:
            print("the queue is empty")
            return

        if self.stack1.length != 0 and self.stack2.length == 0:
            while self.stack1.length != 0:
                p_value = self.stack1.pop()
                self.stack2.push(p_value)

        if self.stack2.length != 0:
            pop_value = self.stack2.pop()
            return pop_value

    def pop_allvalue(self):
        while self.stack1.length != 0 or self.stack2.length != 0:
            value = self.pop()
            yield(value)


    def print_value_another(self):
        if self.stack2.length !=0:
            temp = self.stack2.head
            while temp is not None:
                print(temp.value, "here")
                temp = temp.nexts

        temp_list = []
        if self.stack1.length != 0:
            temp = self.stack1.head
            while temp is not None:
                temp_list.append(temp.value)
                temp = temp.nexts
        for i in temp_list[::-1]:
            print(i, "there")
        return



if __name__ == "__main__":
    """
    mystack = Stack()
    mystack.push(1)
    mystack.push(11)
    mystack.push(8)
    mystack.print_values()
    mystack.pop()
    print("-"*20)
    mystack.print_values()
    print(mystack.length)
    """
    myqueue = MyQueue()
    myqueue.push(1)
    myqueue.push(11)
    myqueue.push(22)

    print(myqueue.pop())
    myqueue.push(44)
    #print(myqueue.pop())
    #print(myqueue.pop())
    #print(myqueue.pop())
    print("*"*20)

    for value in myqueue.pop_allvalue():
        print(value, "no")
    #print(myqueue.print_value())
    #myqueue.print_value_another()