# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = head
        new_head = None
        while temp is not None:
            cur = temp
            temp = temp.next
            cur.next = new_head
            new_head = cur
        return new_head
