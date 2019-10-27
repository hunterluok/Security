

from pythoncode import listnode


class MergeNode:
    def __init__(self):
        pass

    def merge(self, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        merged = None
        if node1.value < node2.value:
            merged = node1
            merged.nexts = self.merge(node1.nexts, node2)
        else:
            merged = node2
            merged.nexts = self.merge(node1, node2.nexts)
        return merged

    @staticmethod
    def print_value(node):
        temp = node
        while temp is not None:
            print(temp.value)
            temp = temp.nexts

class MergeNodeTherr(MergeNode):
    def __init__(self):
        super(MergeNodeTherr, self).__init__()

    def mergethree(self, node1, node2, node3):
        merged = self.merge(node1, node2)
        last = self.merge(merged, node3)
        return last

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1

        if pHead1.value <= pHead2.value:
            merged = pHead1
            pHead1 = pHead1.nexts
        else:
            merged = pHead2
            pHead2 = pHead2.nexts

        temp = merged
        while pHead1 is not None and pHead2 is not None:
            if pHead1.value <= pHead2.value:
                temp.nexts = pHead1
                pHead1 = pHead1.nexts
                temp = temp.nexts
            else:
                temp.nexts = pHead2
                pHead2 = pHead2.nexts
                temp = temp.nexts
        if pHead1 is not None:
            temp.nexts = pHead1
        if pHead2 is not None:
            temp.nexts = pHead2
        return merged



if __name__ == "__main__":
    first = listnode.ListNode()
    second = listnode.ListNode()
    third = listnode.ListNode()

    for i in range(17):
        if i % 3 == 0:
            first.push(i)
        elif i % 3 == 1:
            second.push(i)
        else:
            third.push(i)
    #
    # first.print_value()
    # second.print_value()
    # third.print_value()
    # print("--" * 10)
    # my = MergeNodeTherr()
    # result = my.mergethree(first.head, second.head, third.head)
    # my.print_value(result)
    #
    # print("*"*10)

    aot = Solution()
    res = aot.Merge(first.head, second.head)
    def printnode(node):
        while node is not None:
            print(node.value)
            node = node.nexts
    printnode(res)
