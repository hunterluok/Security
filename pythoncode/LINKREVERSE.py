
from pythoncode.listnode import ListNode


class ReverseNode:
    def __init__(self):
        pass

    def checknode(self, node):
        pass

    def reversenode(self, node):
        temp = node
        new = None
        while temp is not None:
            cur = temp
            temp = temp.nexts
            cur.nexts = new
            new = cur
        return new

    def reverse_k(self, node, k=2):
        if k < 1 or not isinstance(k, int) or node is None:
            return ValueError

        new = None
        temp_new = None

        ano_temp = None
        temp = node
        count = 0
        while temp is not None:
            cur = temp
            temp = temp.nexts
            cur.nexts = temp_new
            temp_new = cur
            count += 1
            if count % k == 0:
                if new is None:
                    new = temp_new
                else:
                    # 设置一个 指针 可以减少遍历的次数。
                    # ano_temp = new
                    if ano_temp is None:
                        ano_temp = new
                    while ano_temp.nexts is not None:
                        print("...", ano_temp.value)
                        ano_temp = ano_temp.nexts
                    ano_temp.nexts = temp_new
                temp_new = None

        # if temp_new is not None:
        #     if new is not None:
        #         ano_temp = new
        #         while ano_temp.nexts is not None:
        #             ano_temp = ano_temp.nexts
        #         ano_temp.nexts = temp_new
        #     else:
        #         new = temp_new

        if temp_new is not None:
            last = None
            while temp_new is not None:
                ncur = temp_new
                temp_new = temp_new.nexts
                ncur.nexts = last
                last = ncur

            ano_temp = new
            if ano_temp is not None:
                while ano_temp.nexts is not None:
                    ano_temp = ano_temp.nexts
                ano_temp.nexts = last
            else:
                new = last
        return new


def printnode(node):
    while node is not None:
        print(node.value)
        node = node.nexts

def print_recursize(node):
    # 反打印链表
    if node is not None:
        print_recursize(node.nexts)
        print(node.value)

if __name__ == "__main__":
    my = ListNode()
    for i in range(4, 33):
        my.push(i)

    my.print_value()
    print("**"*10)
    # my.print_node(my.head)
    nmy = ReverseNode()
    new = nmy.reverse_k(my.head, 3)
    printnode(new)

    print("*" * 10)
    print_recursize(new)