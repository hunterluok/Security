# node


class SingleNode:
    def __init__(self, value=None, nexts=None):
        self.value = value
        self.nexts = nexts


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class ThreeNode:
    def __init__(self, value=None, father=None, left=None, right=None):
        self.value = value
        self.father = father
        self.left = left
        self.right = right

