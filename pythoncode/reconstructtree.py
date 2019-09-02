

class node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class ReconstructTree:
    def __init__(self):
        pass

    def fit(self, preorder, inorders):
        lens = len(preorder)
        # 长度检测
        if lens != len(inorders) or lens < 1:
            raise ValueError("树的元素错误")

        rootvalue = preorder[0]
        mynode = node(rootvalue)
        if len(preorder) == 1 and len(inorders) == 1:
            if preorder[0] == inorders[0]:
                return mynode
            else:
                # 另外一个检测
                raise ValueError("输入不是用一颗树的不同遍历")

        position = inorders.index(rootvalue)
        right_lens = lens - position - 1
        if position > 0:
            # 当 postion 说明没有左子树了
            temp_preorder = preorder[1: position + 1].copy()
            temp_inorder = inorders[0: position].copy()
            mynode.left = self.fit(temp_preorder, temp_inorder)
        if right_lens > 0:
            # 当 right_lens 为0时 说明没有右子树了。
            temp_preorder = preorder[position + 1:].copy()
            temp_inorder = inorders[position+1:].copy()
            mynode.right = self.fit(temp_preorder, temp_inorder)
        return mynode

    @classmethod
    def print_value(cls, tree, test):
        """
        。。
        :param tree: 一颗二叉树
        :param test: 树节点值 按照特定的遍历方式 存入的列表
        :return: 打印节点值
        """
        if tree.left is not None:
            cls.print_value(tree.left, test)
        if tree.right is not None:
            cls.print_value(tree.right, test)
        if tree.value is not None:
            print(tree.value)
            test.append(tree.value)

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
    # preorderx = [1, 2, 4, 7, 3, 5, 6, 8, 11]
    # preorderx = [1, 2, 4, 7, 3, 5, 6]
    # preorderx = [1, 2, 4, 7, 3, 5, 6, 11]
    inorderx = [4, 7, 2, 1, 5, 3, 6, 8]

    #preorderx = [1, 2, 4, 7]
    #inorderx = [4, 7, 2, 1]
    #preorderx = [1, 3, 5, 6, 8]
    #inorderx = [1, 5, 3, 6, 8]
    #preorderx = [1]
    #inorderx = [7]

    model = ReconstructTree()
    res = model.fit(preorderx, inorderx)

    tests = []
    model.print_value(res, tests)
    print("---", tests)

    # model.compare(tests,[1, 5, 3, 6, 8])
    model.compare(tests, preorderx)

