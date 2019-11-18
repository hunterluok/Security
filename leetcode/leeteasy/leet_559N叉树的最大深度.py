"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_dep = 0
        if root is not None:
            max_dep = max_dep + 1
            if root.children is not None:
                for child in root.children:
                    child_dep = self.maxDepth(child) + 1
                    if child_dep > max_dep:
                        max_dep = child_dep
        return max_dep