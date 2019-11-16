"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node'):
        new = []
        if root is not None:
            new.append(root.val)
        else:
            return
        if root.children is not None:
            for child in root.children:
                new.extend(self.preorder(child))
        return new