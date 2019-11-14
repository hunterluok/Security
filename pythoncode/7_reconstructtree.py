

from pythoncode.node import BinaryTreeNode


class ReconstructTree:
    def solve(self):
        pass

    def solution(self, preoder, inorder):
        lens = len(preoder)
        if lens < 1 or lens != len(inorder):
            raise ValueError

        root_value = preoder[0]
        root = BinaryTreeNode(root_value)

        if lens == 1:
            if preoder[0] == inorder[0]:
                return root
            else:
                raise ValueError

        left_len = 0
        while left_len < len(inorder):
            if root_value == inorder[left_len]:
                break
            left_len += 1
        if left_len == len(inorder):
            raise ValueError

        if left_len > 0:
            root.left = self.solution(preoder[1: left_len+1], inorder[0: left_len])
        if len(inorder) > left_len + 1:
            root.right = self.solution(preoder[left_len+1:], inorder[left_len+1: ])
        return root

    @classmethod
    def print_value(cls, node, test=[]):
        if node is not None:
            print(node.data, "--")
            test.append(node.data)
        if node.left is not None:
            cls.print_value(node.left, test)
        if node.right is not None:
            cls.print_value(node.right, test)

    @classmethod
    def print_mid(cls, node):
        if node.left is not None:
            cls.print_mid(node.left)
        if node is not None:
            print(node.data, "--")
        if node.right is not None:
            cls.print_mid(node.right)

    @classmethod
    def compare(cls, lista, listb):
        lens = len(lista)
        if lens != len(listb):
            raise ValueError("两个列表必须相等")
        for i in range(lens):
            if lista[i] != listb[i]:
                print("not passed")
                return
        print("passed")
        return


if __name__ == "__main__":
    preorderx = [1, 2, 4, 7, 3, 5, 6, 8]
    inorderx = [4, 7, 2, 1, 5, 3, 8, 6]
    model = ReconstructTree()
    res = model.solution(preorderx, inorderx)

    tests = []
    model.print_value(res, tests)
    print("---", tests)
    # model.compare(tests,[1, 5, 3, 6, 8])
    model.compare(tests, preorderx)

