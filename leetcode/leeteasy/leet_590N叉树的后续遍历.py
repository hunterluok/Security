"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root):
        new = []
        if root is not None:
            if root.children is not None:
                for child in root.children:
                    new.extend(self.postorder(child))
            new.append(root.val)
        return new