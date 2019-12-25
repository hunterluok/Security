# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.datasets import make_friedman1
from sklearn.ensemble import GradientBoostingRegressor


class treeNode:
    def __init__(self, label_class=None, feature=None, value=None, right_tree=None, left_tree=None):
        self.feature = feature
        self.value = value
        self.right_tree = right_tree
        self.left_tree = left_tree
        self.label_class = label_class
        
    def __name__(self):
        return "treenode"
    
    
class Tree:
    def __init__(self, min_leafs=5, max_depth=10):
        self.min_leafs = min_leafs
        self.max_depth = max_depth
        
    def binsplitdata(self, data, feature, value):
        mat0 = data[data[:, feature] > value, : ]
        mat1 = data[data[:, feature] <= value, : ]
        return mat0, mat1
    
    # 利用字典的方式创建一棵树。
    """
    def createTree_old(self, data, leafType=regleaf, errType=regerr, ops=(1,4)):
        # 这里阐释了如何 利用递归的思想去 建立决策树
        feat, val = self.choosebestsplit(data, leafType, errType, ops)
        # 如果没有可以再次切分的  feature 就返回val
        if feat == None:
            return val
        # 这里注意创建了一个新的 字典？
        retTree = {}
        retTree['spInd'] = feat
        retTree['spVal'] = val
        lSet,rSet = self.binsplitdata(data,feat,val)
        retTree['left'] = self.createTree_old(lSet,leafType,errType, ops)
        retTree['right'] = self.createTree_old(rSet,leafType,errType, ops)
        return retTree
    """
    
    @classmethod
    def get_deep(cls, model):
        max_deep = 0
        if model.right_tree is not None:
            temp_deep = 1 + cls.get_deep(model.right_tree)
            if temp_deep > max_deep:
                max_deep = temp_deep
        if model.left_tree is not None:
            temp_deep = 1 + cls.get_deep(model.left_tree)
            if temp_deep > max_deep:
                max_deep = temp_deep
        return max_deep

    @classmethod
    def print_leafs(cls, model):
        if model.label_class is not None:
            print("leaf value is {}".format(model.label_class))
        if model.left_tree is not None:
            cls.print_leafs(model.left_tree)
        if model.right_tree is not None:
            cls.print_leafs(model.right_tree)

    @classmethod
    def print_featurevalue(cls, model):
        if model.feature is not None:
            print("feature is {} value is {}".format(model.feature, model.value))
        if model.left_tree is not None:
            cls.print_featurevalue(model.left_tree)
        if model.right_tree is not None:
            cls.print_featurevalue(model.right_tree)


    @classmethod
    def predict_line(cls, model, line):
        """
        预测最好不用 递归的调用
        :param model:
        :param line:
        :return:
        """
        if model.label_class is not None:
            return model.label_class
        split_feature = model.feature
        split_value = model.value
        if line[split_feature] > split_value:
            return cls.predict_line(model.right_tree, line)
        else:
            return cls.predict_line(model.left_tree, line)

    @classmethod
    def predict_line_new(cls, model, line):
        temp = model
        while temp.right_tree or temp.left_tree:
            split_feature = temp.feature
            split_value = temp.value
            if line[split_feature] > split_value:
                temp = temp.right_tree
            else:
                temp = temp.left_tree
        if temp.label_class is not None:
            return temp.label_class
        else:
            return "node is wrong"
        
    @classmethod
    def predict(cls, model, data):
        myre = []
        for line in data:
            te = cls.predict_line_new(model, line)
            myre.append(te)
        myre = np.array(myre).reshape(len(data), 1)
        return myre


class CartreeRegression(Tree):
    def __init__(self, min_leafs=4, max_depth=10, max_bins=10):
        super(CartreeRegression, self).__init__()
        self.min_leafs = min_leafs
        self.max_depth = max_depth

        if isinstance(max_bins, int) and max_bins > 1 and max_bins < 50:
            self.max_bins = max_bins
        else:
            raise ValueError("max_bins is not fit for this model")
        
    def regleaf(self, data, epis=3):
        return np.round(np.mean(data[:, -1]), epis)
    
    def regerr(self, data):
        return np.std(data[:, -1])
    
    def createTree(self, data, depth=0):
        retTree = treeNode()
        # 可以添加其他条件,终止树 停止生长，分类和回归树有不同的搞法。
        # 这里阐释了如何 利用递归的思想去 建立决策树
        feat, val = self.choosebestsplit(data)
        # 如果没有可以再次切分的  feature 就返回val
        if feat is None or depth > self.max_depth:
            retTree.label_class = self.regleaf(data)
            return retTree
        retTree.feature = feat
        retTree.value = val
        lset, rset = self.binsplitdata(data, feat, val)
        retTree.left_tree = self.createTree(lset, depth=depth+1)
        retTree.right_tree = self.createTree(rset, depth=depth+1)
        return retTree
    
    def choosebestsplit(self, data):
        data = np.array(data)
        m, n = data.shape

        # 计算初始的方差。
        S = self.regerr(data)
        best_s = np.inf
        best_feat = None 
        best_val = None
    
        for i in range(n-1): # n-1 feature
            # 这么做的好处是 可以加快运行速度，其次可以减少偏态数据的影响，亲测可行，改善预测效果（方差小偏琦大的问题）
            minx = np.min(data[:, i])
            maxs = np.max(data[:, i])
            step = (maxs - minx) / self.max_bins
            value_set = [minx + i * step for i in range(1, self.max_bins)]

            for j in value_set:
            #for j in np.unique(data[:, i]):
                mat0, mat1 = self.binsplitdata(data, i, j)
                # 控制叶子的数量。不进行控制 进行充分的生长
                if (np.shape(mat0)[0] < self.min_leafs) or (np.shape(mat1)[0] < self.min_leafs):
                    continue
                new_s = self.regerr(mat0) + self.regerr(mat1)
                if new_s + 5 < best_s:
                    best_feat = i
                    best_val = j
                    best_s = new_s
                #if S - best_s < 0.01:这个地方需要再思考下
                    #return best_feat, best_val
        return best_feat, best_val


def getMean(tree, i=0, flag=False):
    """
    如果 树的两个分支都不是树的话，求均值就可以了。 value 为none时 label_class一定不为none, 否则已经结束
    """
    if tree.right_tree.value is not None:
        tree.right_tree.label_class = getMean(tree.right_tree, i=i+1)
    if tree.left_tree.value is not None:
        tree.left_tree.label_class = getMean(tree.left_tree, i=i+1)
    means = (tree.right_tree.label_class + tree.left_tree.label_class) / 2.0
    print("level is {} and value is {}".format(i, means))
    return means


def myprune(tree, testData, min_leafs=10, diff_err=10):
    """
    :param tree:
    :param testData:
    :param min_leafs:
    :param diff_err:
    :return:
    """
    def binsplitdata(data, feature, value):
        mat0 = data[data[:, feature] > value, :]
        mat1 = data[data[:, feature] <= value, :]
        return mat0, mat1

    if np.shape(testData)[0] < min_leafs:
        # 这里是有一定的合理性的
        tree.label_class = getMean(tree)
        tree.right_tree = None
        tree.left_tree = None
        tree.value = None
        tree.feature = None
        return tree
    
    if tree.feature is not None:
        lSet, rSet = binsplitdata(testData, tree.feature, tree.value)

        if tree.left_tree.label_class is None: # and lSet.shape[0] > min_leafs:
            tree.left_tree = myprune(tree.left_tree, lSet)
        
        if tree.right_tree.label_class is None:# and rSet.shape[0] > min_leafs:
            tree.right_tree = myprune(tree.right_tree, rSet)


    if tree.left_tree.label_class is not None and tree.right_tree.label_class is not None:
        lSet, rSet = binsplitdata(testData, tree.feature, tree.value)
        errorNoMerge = sum(np.power(lSet[:, -1] - tree.left_tree.label_class, 2)) \
                       + sum(np.power(rSet[:, -1] - tree.right_tree.label_class, 2.0))
        
        # 这里注意 有点意思
        treeMean = (tree.left_tree.label_class + tree.right_tree.label_class) / 2.0
        # 合并之后的 的 方差
        errorMerge = sum(np.power(testData[:,-1] - treeMean, 2))
        m, n = testData.shape
        print("errormerge {}, errornomerge {} m is {} ---".
              format(np.round(errorMerge / m, 2), np.round(errorNoMerge/m, 2), m))
        print((errorMerge - errorNoMerge) / m, "means")
        if (errorMerge - errorNoMerge) / m < diff_err:
        #if errorMerge < errorNoMerge:
            print("merging")
            tree.label_class = treeMean
            tree.right_tree = None
            tree.left_tree = None
            tree.value = None
            tree.feature = None
            return tree
        else:
            return tree
    else:
        return tree


if __name__ == "__main__":
    X, y = make_friedman1(n_samples=1200, random_state=2, noise=2.0)
    x_train, x_test = X[:1000], X[1000: ]#300]
    y_train, y_test = y[:1000], y[1000: ]#300]
    y_train = y_train.reshape((1000, 1))
    data = np.concatenate([x_train, y_train], axis=1)
    y_test = y_test.reshape((x_test.shape[0], 1))
    testdata = np.concatenate([x_test, y_test], axis=1)

    mymodel = CartreeRegression(min_leafs=5 , max_bins=10)
    result = mymodel.createTree(data)

    # sx = myprune(result, testdata, min_leafs=50, diff_err=2)
    # print("tree depth is ", mymodel.get_deep(sx))
    # mymodel.print_leafs(sx)

    print("-"*20)
    pred_test = mymodel.predict(result, testdata[:, :-1])
    print(mean_squared_error(testdata[:, -1], pred_test), "\n")

    #plt.scatter(np.arange(len(testdata)), testdata[:, -1])
    #plt.scatter(np.arange(len(testdata)), pred_test)
    #plt.show()
    print(mymodel.get_deep(result))
    print(mymodel.print_featurevalue(result))
