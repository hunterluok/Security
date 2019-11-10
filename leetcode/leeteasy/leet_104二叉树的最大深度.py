

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode):
        if root is None:
            return 0

        len_left = 1 + self.maxDepth(root.left)
        len_right = 1 + self.maxDepth(root.right)

        if len_left > len_right:
            max_deep = len_left
        else:
            max_deep = len_right
        return max_deep



