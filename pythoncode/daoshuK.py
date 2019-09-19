# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        temp = head
        temp_another = head
        count = 0
        while temp is not None and count < k:
            temp = temp.next
            count += 1
        if count == k:
            while temp is not None:
                temp = temp.next
                temp_another = temp_another.next
            return temp_another
        else:
            return None

