# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        lens = len(nums)
        if lens < 1:
            return TreeNode(None)
        if lens == 1:
            return TreeNode(nums[0])

        max_value = max(nums)
        root = TreeNode(max_value)
        max_index = nums.index(max_value)
        left_len = max_index
        right_len = lens - max_index - 1
        if left_len > 0:
            root.left = self.constructMaximumBinaryTree(nums[0:max_index])
        if right_len > 0:
            root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        return root