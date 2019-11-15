# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val: int):
        if root is None:
            return None
        if root.val == val:
            return root
        if root.left is not None:
            left_re = self.searchBST(root.left, val)
            if left_re is not None:
                return left_re

        if root.right is not None:
            right_re = self.searchBST(root.right, val)
            if right_re is not None:
                return right_re
        return None

