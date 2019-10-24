

class ListMerge:
    def __init__(self):
        pass

    def get_merge(self, d1, d2):
        if d1[0] > d2[0]:
            return self.merge(d2, d1, start=0, end=0)
        else:
            return self.merge(d1, d2, start=0, end=0)

    def merge(self, data1, data2, start=0, end=0):
        len_d2 = len(data2)
        lens = len(data1)
        while start < lens and end < len_d2 and data1[start] <= data2[end]:
            index = start
            # print("index is {}".format(index))
            while index < lens and data[index] <= data2[end]:
                index += 1
            data1.insert(index, data2[end])
            lens = len(data1)
            start = index
            end += 1
        return data1


class ListMergeTwo(ListMerge):
    def __init__(self):
        super(ListMergeTwo, self).__init__()

    def merge(self, d1, d2, start=0, end=0):
        """
        利用递归的方式 进行数据的插入。
        :param d1:
        :param d2:
        :param start:
        :param end:
        :return:
        """
        len1 = len(d1)
        len2 = len(d2)
        if start >= len1 or end >= len2:
            return d1

        index = start
        while index < len1 and d1[index] <= d2[end]:
            index += 1
        d1.insert(index, d2[end])
        print("end is {}".format(end))
        print("index is {}".format(index))
        self.merge(d1, d2, start=index, end=end+1)
        return d1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1

        merged = None
        if node1.val <= node2.val:
            merged = node1
            merged.next = self.merge(node1.next, node2)
        else:
            merged = node2
            merged.next = self.merge(node1, node2.next)
        return merged

    def merge_ano(self, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1

        if node1.val <= node2.val:
            merged = node1
            node1 = node1.next
        else:
            merged = node2
            node2 = node2.next

        temp = merged
        while node1 is not None and node2 is not None:
            if node1.val <= node2.val:
                temp.next = node1
                node1 = node1.next
                temp = temp.next
            else:
                temp.next = node2
                node2 = node2.next
                temp = temp.next
        if node1 is not None:
            temp.next = node1
        if node2 is not None:
            temp.next = node2
        return merged

    def mergeKLists(self, lists):
        lens = len(lists)
        if lens == 1:
            return lists[0]
        if lens == 0:
            return None

        last = self.merge_ano(lists[0], lists[1])
        for i in range(2, lens):
            last = self.merge_ano(last, lists[i])
            # last = temp
        return last


if __name__ == "__main__":
    #my = ListMerge()
    #data = [1, 3, 5, 7]
    #data2 = [2, 3, 4, 4, 8, 9, 10, 11]
    #print(my.merge(data, data2))

    my = ListMerge() #Two()
    data = [1, 3, 5, 7]
    data2 = [2, 3, 4, 4, 8, 9, 22, 31]
    print(my.get_merge(data, data2))


