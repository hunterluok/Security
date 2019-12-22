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
    def __init__(self, value=None, feature=None, father=None, left=None, right=None):
        self.value = value
        self.feture = feature
        self.father = father
        self.left = left
        self.right = right


class KdNode:
    def __init__(self, data=None, value=None, feature=None, father=None, left=None, right=None):
        self.data = data
        self.value = value
        self.feature = feature
        self.father = father
        self.left = left
        self.right = right


