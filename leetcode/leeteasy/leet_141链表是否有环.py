# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        temp = head
        if temp is None:
            return False
        
        temp_2 = head
        if temp_2.next is None:
            return False
        else:
            temp_2 = temp_2.next

        while temp is not None and temp_2 is not None:
            if temp.val == temp_2.val:
                return True
            else:
                temp = temp.next
                if temp_2.next is not None:
                    temp_2 = temp_2.next.next
                else:
                    return False
        return False



